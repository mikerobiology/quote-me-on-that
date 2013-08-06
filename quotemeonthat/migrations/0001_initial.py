# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table(u'quotemeonthat_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('catalog_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('item_description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('list_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2)),
            ('discount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2)),
            ('net_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2)),
            ('quote_expires', self.gf('django.db.models.fields.DateField')()),
            ('expired', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'quotemeonthat', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'quotemeonthat_quote')


    models = {
        u'quotemeonthat.quote': {
            'Meta': {'object_name': 'Quote'},
            'catalog_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2'}),
            'expired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'list_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2'}),
            'net_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2'}),
            'quote_expires': ('django.db.models.fields.DateField', [], {}),
            'quote_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['quotemeonthat']