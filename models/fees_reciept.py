from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Create_member(models.Model):
    _name = "games.fees"
    _description = "sports club"


    name = fields.Many2one("create.member",string="Name")
    lname = fields.Char(string="Last Name",related="name.lname")

    age = fields.Integer(string="Member Age",related="name.age")
    phone = fields.Char(string="Phone no +91",related="name.phone")
    email = fields.Char(string="Email",related="name.email")
    game = fields.Many2one("sports.game", string="Game",related="name.game")
    month = fields.Integer(string="Month",related="name.month")
    star_date = fields.Date(string="Starting Date",related="name.star_date")
    end_date = fields.Date(string="Ending Date")
    fees = fields.Integer(string="fees",related="name.fees")
    youpaid=fields.Integer(string="You Paid")
    gst=fields.Integer(string="GST")
    discount=fields.Char(string="discount")
    total=fields.Integer(string="t")

    @api.onchange("name")
    def onchange_fees(self):
        if self.name:
            self.total=self.name.fees*self.name.month
            self.discount= self.discount
            self.gst= self.total*(18/100)
            self.youpaid = self.name.fees*self.name.month + self.gst
            self.end_date = (datetime.strptime(str(self.name.star_date), '%Y-%m-%d') + relativedelta(
                months=self.name.month)).strftime('%Y-%m-%d')
