# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:06:28 2018

@author: EA-ShevchenkoIS
"""

import random

class Lessons():
    def __init__(self):
        self.lessons = ['les_{:0>2d}'.format(i) for i in range(1,14)]
        self.used_lessons = set()
        self.all_lessons = None
    
    def __repr__(self):
        return str(self.holder)
    
    def __choose_totalhours(self):
        hours = [16, 32, 48]
        return hours[random.randint(0,2)]    
    
    def __choose_lesson(self):
        while True:
            les = self.lessons[random.randint(0, len(self.lessons)-1)]
            if les not in self.used_lessons:
                self.used_lessons.add(les)
                break
        return les
    
    def create_lessons(self):
        if self.holder:
            return self.holder
        holder = []
        while len(self.used_lessons) < 13:
            holder.append((self.__choose_lesson(), self.__choose_totalhours()))
        self.all_lessons = sorted(holder, key=lambda x: x[0])
        return self.all_lessons
                          
class Classrooms():
    def __inir__(self):
        self.rooms = ['room_{:0>3d}'.format(i) for i in range(18)]
    
    def __repr__(self):
        return str(self.rooms)
    
    def choose_room(self):
        room = self.rooms.pop()
        self.rooms = room + self.rooms
        return room

class Professor():
    alph = [chr(i) for i in range(97, 123, 1)]
    def __init__(self, lesson):
        self.name = self.__create_name()
        self.lesson = lesson
    
    def __create_name(self):
        name_letters = random.choices(Professor.alph, k=random.randint(3,8))
        return ''.join(name_letters).capitalize()
    
    def __repr__(self):
        return (
                'Prof.: {: >8s}, lesson: {: >6s}'.format(self.name, self.lesson)
                )


class Week():
    pass

class Day():
    def __init__(self, **lessons):
        self.lessons = lessons

class StudyGroup():
    def __init__(self, name):
        self.name = name