# -*- coding: utf-8 -*-
import requests

from odoo import api, fields, models, _, tools


class Diet(models.Model):
    _name = "diet"
    _description = "Diet"

    name = fields.Text('Name', required=True)

class Ingredient(models.Model):
    _name = "ingredient"
    _description = "Ingredient"

    name = fields.Text('Name', required=True)

    def import_ingredients(self):
        url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

        headers = {
            'x-rapidapi-key': "0f1c9a6651mshcc6fb880746f7d2p18a345jsna7eda5bbbed3",
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
        return response