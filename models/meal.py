# -*- coding: utf-8 -*-
import requests

from odoo import api, fields, models, _, tools

class Meal(models.Model):
    _name = "meal"
    _description = "Meal"

    name = fields.Text('Name', required=True)
    aliment_ids = fields.Many2many('aliment', 'aliment_id', string="Ingredients")
