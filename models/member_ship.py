from odoo import models,fields,api
from datetime import date


class Create_member(models.Model):
    _name = "create.member"
    _description = "sports club"


    name=fields.Char(string="First Name",)
    lname=fields.Char(string="Last Name")
    age=fields.Integer(string="Member Age")
    phone=fields.Char(string="Phone no +91")
    email=fields.Char(string="Email")
    game=fields.Many2one("sports.game",string="Game")
    month=fields.Integer(string="Month")
    star_date=fields.Date(string="Starting Date")
    fees=fields.Integer(string="fees")
    end_date = fields.Date(string="Ending Date")





    @api.onchange("game")
    def onchange_fees(self):
        if self.game:
            self.update({'fees':self.game.fees})


