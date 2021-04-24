# -*- coding: utf-8 -*-
import requests

from odoo import api, fields, models, _, tools

class Diet(models.Model):
    _name = "diet"
    _description = "Diet"

    name = fields.Text('Name', required=True)
    creator = fields.Many2one('res.users', string="Creator", default=lambda self: self.env.user.id)
    assigned_to = fields.Many2many('res.users', 'res_user_id', string="Assigned to")
    type = fields.Many2one('diet.type', string="Type", store=True, readonly=False)
    public = fields.Boolean(string='Public')
    monday_diet_id = fields.Many2one('daily.diet', string="Monday", store=True, readonly=False)
    tuesday_diet_id = fields.Many2one('daily.diet', string="Tuesday", store=True, readonly=False)
    wednesday_diet_id = fields.Many2one('daily.diet', string="Wednesday", store=True, readonly=False)
    thursday_diet_id = fields.Many2one('daily.diet', string="Thursday", store=True, readonly=False)
    friday_diet_id = fields.Many2one('daily.diet', string="Friday", store=True, readonly=False)
    saturday_diet_id = fields.Many2one('daily.diet', string="Saturday", store=True, readonly=False)
    sunday_diet_id = fields.Many2one('daily.diet', string="Sunday", store=True, readonly=False)


class DietType(models.Model):
    _name = "diet.type"
    _description = "Diet type"
    name = fields.Text('Name', required=True)