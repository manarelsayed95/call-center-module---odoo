# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Calls(models.Model):
    _name = 'call_center.calls'
    _description = 'calls'

    start_time=fields.Datetime()
    stop_time=fields.Datetime()
    duration=fields.Float(compute='_compute_duration' , store=True)
    source=fields.Char()
    destination=fields.Char()
    name=fields.Char(default='New')
    station=fields.Many2one(comodel_name='call_center.station')
    tags=fields.Many2many(comodel_name='call_center.tags')
    state=fields.Selection([
    	('draft','Draft'),
    	('invoiced','Invoiced'),

    ],default='draft',string='Status')

@api.constrains('stop_time')
def checkStopTime(self):
	for rec in self:
		if rec.stop_time < rec.start_time:
			raise ValidationError('Stop time should be bigger than start time!')

@api.depends('start_time','stop_time')
def _compute_duration(self):
	for rec in self:
		rec.duration=(rec.stop_time-rec.start_time).seconds/60

# class Station(models.Model):
# 	_name='call_center.station'

# 	name=fields.Char()
# 	calls=fields.One2many(comodel_name='call_center.calls',inverse_name='station')

class Tags(models.Model):
	_name='call_center.tags'
    
	name=fields.Char()