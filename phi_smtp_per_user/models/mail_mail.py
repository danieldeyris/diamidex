# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import _, api, fields, models
from odoo import tools
from odoo.addons.base.models.ir_mail_server import MailDeliveryException
from collections import defaultdict

_logger = logging.getLogger(__name__)


class MailMail(models.Model):
    _inherit = 'mail.mail'

    def send(self, auto_commit=False, raise_exception=False):
        # select smtp mail server from author email address
        for mail in self:
            if not mail.mail_server_id and mail.author_id and mail.author_id.email:
                mail.mail_server_id = self.env["ir.mail_server"].sudo().search([('smtp_user', '=', mail.author_id.email)], limit=1)

        return super(MailMail, self).send(auto_commit=False, raise_exception=False)
