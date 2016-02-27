#!/usr/bin/env python3

import sys
import os
import re

def getRejectedUsers():
    all_list=[]
    rej_list=[]
    count1=0
    count2=0
    expr1 = r"(.*),, , ;,; ;,; ;,;, ;,; ,,(.*)" #extract names
    with open("SiteRegistration.txt") as inputFile:
        content = inputFile.readlines()
        for line in content:
            #print(line)
            matched1 = re.search(expr1,line)
            if matched1:
                count1+=1
                name= matched1.group(1)
                last=matched1.group(2)
                if(last == ""):
                    all_list.append(name)
            else:
                count2+=1

    #print(all_list)
    expr2 = r"(\w+),\s(\w+)"
    for name in all_list:
        matched2 = re.search(expr2,name)
        if matched2:
            new_name=matched2.group(2)+" "+matched2.group(1)
            rej_list.append(new_name)
        else:
            rej_list.append(name)
    #print(rej_list)
    rej_list.sort()
    return rej_list

def getUsersWithEmails():
    final_dict={}
    email_list=[]
    name_list=[]
    final_name_list=[]
    expr1 = r"(.*),, , ,,(.*), ;(.*)" #extract names
    expr2 = r"[\w\s]+,\s?[\s\w+]?,,?\s\, ,,([\w@.]+),(.*)" #have emails
    with open("SiteRegistration.txt") as inputFile:
        content = inputFile.readlines()
        for line in content:

            matched2 = re.search(expr2,line)
            if matched2:

                # GET EMAILS
                email= matched2.group(1)
                #print(email)
                email_list.append(email)

                # GET NAMES
                matched1 = re.search(expr1,line)
                if matched1:
                    name= matched1.group(1)
                    name_list.append(name)
    expr3 = r"(\w+),\s(\w+)"
    for name in name_list:
        matched3 = re.search(expr3,name)
        if matched3:
            new_name=matched3.group(2)+" "+matched3.group(1)
            final_name_list.append(new_name)
        else:
            final_name_list.append(name)
    #print(final_name_list)
    #print(email_list)
    for i in range(len(final_name_list)):
        final_dict[final_name_list[i]]=email_list[i]
    return final_dict

def getUsersWithPhones():
    final_dict={}
    phone_list=[]
    name_list=[]
    final_name_list=[]
    final_phone_list=[]
    expr1 = r"(.*),, , ,,(.*), ;,; ,(.*);,; ;,(.*)" #phone is matched1.group(3)
    expr2 = r"(.*),, , ;,; ;,; ,(.*);,; ;,;(.*)" #phone is matched2.group(2)
    with open("SiteRegistration.txt") as inputFile:
        content = inputFile.readlines()
        for line in content:

            matched2 = re.search(expr2,line)
            matched1 = re.search(expr1,line)
            if matched2:
                phone = matched2.group(2)
                name= matched2.group(1)
                name_list.append(name)
            elif(matched1):
                phone = matched1.group(3)
                name= matched1.group(1)
                name_list.append(name)
            else:
                phone="NO"
            if(phone != "NO"):
                phone_list.append(phone)
    expr4=r"(\d{3})(\d{3})(\d{4})"
    expr5=r"(\d{3})-(\d{3})-(\d{4})"
    for number in phone_list:
        matched4 = re.search(expr4,number)
        matched5 = re.search(expr5,number)
        if matched4:
            phone="("+matched4.group(1)+") "+matched4.group(2)+"-"+matched4.group(3)
            final_phone_list.append(phone)
            #print(phone)
        elif matched5:
            phone="("+matched5.group(1)+") "+matched5.group(2)+"-"+matched5.group(3)
            final_phone_list.append(phone)
            #print(phone)
        else:
            final_phone_list.append(number)

    expr3 = r"(\w+),\s(\w+)"
    for name in name_list:
        matched3 = re.search(expr3,name)
        if matched3:
            new_name=matched3.group(2)+" "+matched3.group(1)
            final_name_list.append(new_name)
        else:
            final_name_list.append(name)

    #print(final_phone_list)
    for i in range(len(final_name_list)):
        final_dict[final_name_list[i]]=final_phone_list[i]
    return final_dict

def getUsersWithStates():
    expr1 = r"(.$)"
    expr2 = r"(.*)*,,(.*)$"
    expr4 = r"(.*),, ,(.*)"
    final_dict={}
    state_list=[]
    name_list=[]
    final_name_list=[]


    with open("SiteRegistration.txt") as inputFile:
        content = inputFile.readlines()
        for line in content:
            matched1 = re.search(expr1,line)
            if matched1:
                if(matched1.group(1) != ","):
                    matched2 = re.search(expr2,line)
                    if matched2:
                        state_list.append(matched2.group(2))
                        matched4=re.search(expr4,line)
                        if matched4:
                            name= matched4.group(1)
                            name_list.append(name)
    expr3 = r"(\w+),\s(\w+)"
    for name in name_list:
        matched3 = re.search(expr3,name)
        if matched3:
            new_name=matched3.group(2)+" "+matched3.group(1)
            final_name_list.append(new_name)
        else:
            final_name_list.append(name)

    #print(final_phone_list)
    for i in range(len(final_name_list)):
        final_dict[final_name_list[i]]=state_list[i]
    return final_dict

def getUsersWithoutEmails():
    email_dict=getUsersWithEmails()
    phone_dict=getUsersWithPhones()
    state_dict=getUsersWithStates()
    final_dict={}
    final_list=[]

    #print("-----------------------PHONE AND NO EMAIL")
    for key in phone_dict:
        if key not in email_dict:
            #print(key)
            final_list.append(key)

    #print("-----------------------STATE AND NO EMAIL")
    for key in state_dict:
        if key not in email_dict:
            #print(key)
            final_list.append(key)

    final_list.sort()
    final_set=set(final_list)
    new_list=list(final_set)
    new_list.sort()
    return new_list

def getUsersWithoutPhones():
    return 0

def getUsersWithoutStates():
    return 0

def getUsersWithCompleteInfo():
    email_dict=getUsersWithEmails()
    phone_dict=getUsersWithPhones()
    state_dict=getUsersWithStates()
    final_dict={}

    for key in email_dict:
        if key in phone_dict:
            if key in state_dict:
                final_dict[key]=(email_dict[key], phone_dict[key], state_dict[key])
    return final_dict

