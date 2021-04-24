# -*- coding: utf-8 -*-
import requests

from odoo import api, fields, models, _, tools

class DailyDiet(models.Model):
    _name = "daily.diet"
    _description = "Dialy Diet"

    name = fields.Text('Name', required=True)
    meal_ids = fields.Many2many('meal', 'meal_id', string="Meals")
