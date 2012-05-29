#!/usr/bin/env python
#
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import db

class Post(db.Model):
  first_name = db.StringProperty()
  last_name = db.StringProperty()
  email = db.EmailProperty()
  phone = db.PhoneNumberProperty()
  pref_book = db.StringProperty()
  osys = db.StringProperty()
  created_on = db.DateTimeProperty(auto_now_add = 1)
