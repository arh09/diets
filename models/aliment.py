# -*- coding: utf-8 -*-
import requests

from odoo import api, fields, models, _

class Aliment(models.Model):
    _name = "aliment"
    _description = "Aliment"

    name = fields.Text('Name', required=True)
    line_ids = fields.Many2many('aliment.line', 'aliment_line_id', string="Components")
    group = fields.Many2one('aliment.group', string="Group", store=True, readonly=False)

    def import_aliments(self):
        url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

        headers = {
            'x-rapidapi-key': "0f1c9a6651mshcc6fb880746f7d2p18a345jsna7eda5bbbed3",
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
        return response

class AlimentGroup(models.Model):
    _name = "aliment.group"
    _description = "Aliment Group"

    name = fields.Text('Name', required=True)

class AlimentLine(models.Model):
    _name = "aliment.line"
    _description = "Aliment Line"

    value = fields.Integer('Value', required=True)
    unit = fields.Text('Unit', required=True)
    component_id = fields.Many2one('component', string="Component", store=True, readonly=False)
