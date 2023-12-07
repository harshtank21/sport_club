from odoo import models,fields,api


class Create_member(models.Model):
    _name = "sports.game"
    _description = "sports club"


    name=fields.Char(string="Games Name")
    fees=fields.Integer(string="fees")
    members=fields.Integer(string="members")



