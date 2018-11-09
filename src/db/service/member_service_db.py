# coding: utf-8

import logging
import datetime
from member import Member
from member_repo import MemberRepo


class MemberServiceDb(object):
    @staticmethod
    def load_members(names):
        for name in names:
            member = MemberRepo.get_member_by_name(name)
            if member is None:
                last_num = MemberServiceDb.get_member_last_number()
                now = datetime.datetime.today().strftime('%Y-%m-%d')
                member = Member(last_num, name, now)
                MemberRepo.insert_member(member)
            else:
                logging.warning('Member with name [' + name + "] already exists in database")

    @staticmethod
    def get_member_last_number():
        last = 0
        last_member = MemberRepo.get_last_member()
        if last_member is not None:
            last = last_member.number
        return last
