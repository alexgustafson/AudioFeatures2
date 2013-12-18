# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TextContent'
        db.create_table(u'af_documentation_textcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('main_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'af_documentation', ['TextContent'])

        # Adding model 'FigureContent'
        db.create_table(u'af_documentation_figurecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'af_documentation', ['FigureContent'])

        # Adding model 'ContentNode'
        db.create_table(u'af_documentation_contentnode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent_section', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Content', null=True, to=orm['af_documentation.Section'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='text', max_length=10)),
            ('text_content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['af_documentation.TextContent'])),
            ('figure_content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['af_documentation.FigureContent'])),
        ))
        db.send_create_signal(u'af_documentation', ['ContentNode'])


    def backwards(self, orm):
        # Deleting model 'TextContent'
        db.delete_table(u'af_documentation_textcontent')

        # Deleting model 'FigureContent'
        db.delete_table(u'af_documentation_figurecontent')

        # Deleting model 'ContentNode'
        db.delete_table(u'af_documentation_contentnode')


    models = {
        u'af_documentation.contentnode': {
            'Meta': {'object_name': 'ContentNode'},
            'figure_content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['af_documentation.FigureContent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent_section': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Content'", 'null': 'True', 'to': u"orm['af_documentation.Section']"}),
            'text_content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['af_documentation.TextContent']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '10'})
        },
        u'af_documentation.figurecontent': {
            'Meta': {'object_name': 'FigureContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'af_documentation.section': {
            'Meta': {'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'main_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['af_documentation.Section']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'af_documentation.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_ref': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'af_documentation.textcontent': {
            'Meta': {'object_name': 'TextContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['af_documentation']