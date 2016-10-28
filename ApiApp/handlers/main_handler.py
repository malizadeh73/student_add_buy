#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado
from models import *


class add_buy_Handler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self, *args, **kwargs):

        payer_id = self.get_argument('payer')
        amount = self.get_argument('amount')
        concern = self.get_argument('concern')
        partners = self.get_arguments('partners')
        partners = partners[0].split(',')
        date = self.get_argument('date')
        count = len(partners)
        per_share = int(amount)/count
        bool_accept = False

        for i in self.request.arguments:
            if self.get_argument(i, None) == "":
                self.write(" لطفا همه فیلدها را پر کنید. ")
                bool_accept = True
                return

        if not bool_accept:
            buy = Buy.create(
                amount=amount,
                concern=concern,
                date=date,
                payer_id=payer_id,
                per_share=per_share
            )
            for i in partners:
                User_has_buy.create(
                    User=i,
                    Buy=buy.id
                )

            for i in partners:
                try:
                    find_user = User.select().where(User.id == i).get()
                    find_user = find_user.account
                except:
                    find_user = False
                account2 = per_share + int(find_user)
                update_account = User.update(account=account2).where(User.id == i)
                update_account.execute()

        self.write("ثبت هزینه با موفقیت انجام شد.")