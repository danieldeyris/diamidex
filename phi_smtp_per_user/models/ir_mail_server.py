# -*- coding: utf-8 -*-
# Copyright 2014 wangbuke <wangbuke@gmail.com>
# Copyright 2017 Jarvis <jarvis@odoomod.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, models, tools


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False):
        # Get mail server from user email
        if not mail_server_id:
            mail_server_id = self.sudo().search()

        return super(IrMailServer, self).send_email(message, mail_server_id, smtp_server, smtp_port,
                                                    smtp_user, smtp_password, smtp_encryption, smtp_debug)
