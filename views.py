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

import datetime
import re

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse

from google.appengine.api import users

from models import Post
from forms import ChoiceForm

telephoneExpression = \
   re.compile( r'^\(\d{3}\)\d{3}-\d{4}$' )

def index(request):
  form = ChoiceForm()
  return render_to_response('index.html',
                            {
                             'form': form
                            }
                           )
def listall(request):
  query = Post.gql('ORDER BY created_on DESC')
  return render_to_response('all.html',
                            {'posts': query.fetch(100)
                            }
                           )                          
         

def sign(request):
  form = ChoiceForm(request.POST)
  if form.is_valid():
   if telephoneExpression.match(form.clean_data['phone']):
     fre = {'fname': form.clean_data['first_name'], 'lname': form.clean_data['last_name'], 
     'email': form.clean_data ['email'], 'phone': form.clean_data['phone'], 
     'pref_book': form.clean_data['pref_book'], 
     'osys': form.clean_data['osys']}
    
     post = Post(first_name=form.clean_data['first_name'], last_name=form.clean_data['last_name'],
     email=form.clean_data['email'], phone=form.clean_data['phone'],
     pref_book=form.clean_data['pref_book'], osys=form.clean_data['osys'])
     post.put()

     return render_to_response('thanks.html', fre
                            )
   else:
     return render_to_response('err.html')
  else:
     return render_to_response('err.html')  
  
def detail(request, book_id):
    q = Post.gql('WHERE pref_book IN (\'%s\')' % book_id)
    return render_to_response('getbybook.html', {'posts': q.fetch(100)
                            }
                            )
def osdetail(request, book_id):
    q = Post.gql('WHERE osys IN (\'%s\')' % book_id)
    return render_to_response('getbybook.html', {'posts': q.fetch(100)
                            }
                            )
