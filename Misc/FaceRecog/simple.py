#!/usr/bin/env python2
# coding:utf-8
import face_recognition
image = face_recognition.load_image_file('biden.jpg')
face_location = face_recognition.face_locations(image)
print(face_location)