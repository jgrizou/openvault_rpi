import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# adding openvault directory to path
import sys
openvault_path = os.path.join(HERE_PATH, '..', '..', '..')
sys.path.append(openvault_path)

import random

from flask import request
from flask_socketio import Namespace, emit

from tools import read_config

from openvault.discrete import DiscreteLearner


class LearnerManager(Namespace):

    def __init__(self, socketio, namespace='/'):
        super().__init__(namespace)
        self.socketio = socketio
        self.learners = {}

    def spawn(self, room_id, config_filename):
        if room_id in self.learners:
            self.kill(room_id)
        self.learners[room_id] = Learner(self.socketio, room_id, config_filename)

    def kill(self, room_id):
        if room_id in self.learners:
            del(self.learners[room_id])

    def on_log(self, data):
        room_id = request.sid
        print('[{}] {}'.format(room_id, data))

    def on_is_spawn(self):
        room_id = request.sid
        emit('spawn_state', room_id in self.learners)

    def on_reset(self):
        room_id = request.sid
        if room_id in self.learners:
            self.learners[room_id].reset()

    def on_feedback_info(self, feedback_info):
        room_id = request.sid
        if room_id in self.learners:
            self.learners[room_id].step(feedback_info)


class Learner(object):

    def __init__(self, socketio, room_id, config_filename):
        self.socketio = socketio
        self.room_id = room_id
        self.config_filename = config_filename
        self.reset()

    def reset(self):
        print('[{}] Loading {}'.format(self.room_id, self.config_filename))
        self.config = read_config(self.config_filename)
        self.code_manager = CodeManager(self.config['code'])
        self.init_learner()
        self.start()

    def init_learner(self):
        learner_info = self.config['learner']
        if learner_info['type'] == 'discrete':
            self.learner = DiscreteLearner(
                learner_info['n_hypothesis'],
                learner_info['known_symbols'])
        else:
            raise Exception('Learner of type {} not handled'. format(learner_info['type']))

    def start(self):
        self.update_iteration(new_iteration_value=0)
        self.update_code(apply_pause=False)
        self.update_pad()
        self.update_flash_pattern()
        print('Starting learner...')

    def step(self, feedback_info):
        if self.code_manager.is_code_decoded():
            raise Exception('Should never get there')
        else:
            self.update_iteration(self.n_iteration + 1)

            self.update_learner(feedback_info)

            if self.learner.is_inconsistent():
                self.socketio.emit('inconsistent', room=self.room_id)

            if self.learner.is_solved():
                self.update_code()
                self.update_known_symbols()
                # restart the learner for next number
                self.init_learner()

                print(self.config['learner']['known_symbols'])
                print(self.code_manager.decoded_code)

            if self.code_manager.is_code_decoded():
                if self.code_manager.is_code_valid():
                    self.socketio.emit('valid', room=self.room_id)
                else:
                    self.socketio.emit('invalid', room=self.room_id)
            else:
                self.update_pad()
                self.update_flash_pattern()

    def update_known_symbols(self):
        # update the known_symbols if needed
        learner_info = self.config['learner']
        if learner_info['accumulate_known_symbols_between_numbers']:
            solution_index = self.learner.get_solution_index()
            learner_info['known_symbols'] = self.learner.compute_symbols_belief_for_hypothesis(solution_index)
        print(self.config['learner'])

    def update_iteration(self, new_iteration_value):
        self.n_iteration = new_iteration_value
        self.socketio.emit('n_iteration', self.n_iteration, room=self.room_id)

    def update_flash_pattern(self):
        self.socketio.emit(
            'update_flash',
            self.learner.get_next_flash_pattern(),
            room=self.room_id)

    def update_learner(self, feedback_info):

        displayed_flash_patterns = feedback_info['flash']
        feedback_symbol = feedback_info['symbol']

        # print('##### Updating {} for {} with {}'.format(self.room_id, displayed_flash_patterns, feedback_symbol))

        self.learner.update(displayed_flash_patterns, feedback_symbol)

    def update_code(self, apply_pause=True):
        # if new digit found
        if self.learner.is_solved():
            solution_index = self.learner.get_solution_index()
            self.code_manager.add_new_digit(solution_index)

        code_info = {}
        code_info['code_json'] = self.code_manager.code_json
        code_info['apply_pause'] = apply_pause

        self.socketio.emit(
            'update_code',
            code_info,
            room=self.room_id)

    def update_pad(self):
        pad_info = self.config['pad']
        if pad_info['show_learning_progress']:
            learner_info = self.config['learner']
            known_symbols = learner_info['known_symbols']

            FLASH_TO_COLOR = {}
            FLASH_TO_COLOR[True] = 'flash'
            FLASH_TO_COLOR[False] = 'noflash'

            pad_color = ['neutral' for _ in range(pad_info['n_pad'])]
            for k, v in known_symbols.items():
                pad_color[int(k)] = FLASH_TO_COLOR[v]
            print(pad_color)
            self.socketio.emit('update_pad', pad_color, room=self.room_id)


class CodeManager(object):

    def __init__(self, code_config):
        self.config =  code_config
        self.reset()

    def reset(self):
        self.decoded_code = [None for _ in self.secret_code]
        self.ongoing_digit_index = 0

    def add_new_digit(self, digit):
        self.decoded_code[self.ongoing_digit_index] = digit
        self.ongoing_digit_index += 1

    def is_code_decoded(self):
        return not None in self.decoded_code

    def is_code_valid(self):
        return self.secret_code == self.decoded_code

    @property
    def secret_code(self):
        return self.config['secret_code']

    @property
    def code_json(self):
        code_json = []
        ongoing_not_set = True

        for digit in self.decoded_code:
            digit_json = {
                'found': False,
                'ongoing': False,
                'text': ''
            }

            if digit is None:
                if ongoing_not_set:
                    digit_json['ongoing'] = True
                    ongoing_not_set = False
            else:
                if self.config['show_code']:
                    digit_json['text'] = str(digit)
                else:
                    digit_json['text'] = '#'

            code_json.append(digit_json)

        return code_json
