# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quote.list_price'
        db.add_column(u'quotemeonthat_quote', 'list_price',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Quote.discount'
        db.add_column(u'quotemeonthat_quote', 'discount',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Quote.net_price'
        db.add_column(u'quotemeonthat_quote', 'net_price',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=100, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Quote.list_price'
        db.delete_column(u'quotemeonthat_quote', 'list_price')

        # Deleting field 'Quote.discount'
        db.delete_column(u'quotemeonthat_quote', 'discount')

        # Deleting field 'Quote.net_price'
        db.delete_column(u'quotemeonthat_quote', 'net_price')


    models = {
        u'quotemeonthat.quote': {
            'Meta': {'object_name': 'Quote'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'catalog_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'list_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'net_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'quote_expires': ('django.db.models.fields.DateField', [], {}),
            'quote_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['quotemeonthat']