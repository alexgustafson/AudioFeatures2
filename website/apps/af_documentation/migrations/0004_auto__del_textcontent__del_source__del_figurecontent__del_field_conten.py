# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TextContent'
        db.delete_table(u'af_documentation_textcontent')

        # Deleting model 'Source'
        db.delete_table(u'af_documentation_source')

        # Deleting model 'FigureContent'
        db.delete_table(u'af_documentation_figurecontent')

        # Deleting field 'ContentNode.figure_content'
        db.delete_column(u'af_documentation_contentnode', 'figure_content_id')

        # Deleting field 'ContentNode.text_content'
        db.delete_column(u'af_documentation_contentnode', 'text_content_id')

        # Deleting field 'ContentNode.type'
        db.delete_column(u'af_documentation_contentnode', 'type')

        # Adding field 'ContentNode.body'
        db.add_column(u'af_documentation_contentnode', 'body',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'ContentNode.content_type'
        db.add_column(u'af_documentation_contentnode', 'content_type',
                      self.gf('djangoplugins.fields.PluginField')(default=0, point=orm['djangoplugins.Plugin']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'TextContent'
        db.create_table(u'af_documentation_textcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('main_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'af_documentation', ['TextContent'])

        # Adding model 'Source'
        db.create_table(u'af_documentation_source', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source_ref', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'af_documentation', ['Source'])

        # Adding model 'FigureContent'
        db.create_table(u'af_documentation_figurecontent', (
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'af_documentation', ['FigureContent'])


        # User chose to not deal with backwards NULL issues for 'ContentNode.figure_content'
        raise RuntimeError("Cannot reverse this migration. 'ContentNode.figure_content' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContentNode.figure_content'
        db.add_column(u'af_documentation_contentnode', 'figure_content',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['af_documentation.FigureContent']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ContentNode.text_content'
        raise RuntimeError("Cannot reverse this migration. 'ContentNode.text_content' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ContentNode.text_content'
        db.add_column(u'af_documentation_contentnode', 'text_content',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['af_documentation.TextContent']),
                      keep_default=False)

        # Adding field 'ContentNode.type'
        db.add_column(u'af_documentation_contentnode', 'type',
                      self.gf('django.db.models.fields.CharField')(default='text', max_length=10),
                      keep_default=False)

        # Deleting field 'ContentNode.body'
        db.delete_column(u'af_documentation_contentnode', 'body')

        # Deleting field 'ContentNode.content_type'
        db.delete_column(u'af_documentation_contentnode', 'content_type_id')


    models = {
        u'af_documentation.contentnode': {
            'Meta': {'object_name': 'ContentNode'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'content_type': ('djangoplugins.fields.PluginField', [], {'point': u"orm['djangoplugins.Plugin']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_section': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Content'", 'null': 'True', 'to': u"orm['af_documentation.Section']"})
        },
        u'af_documentation.section': {
            'Meta': {'object_name': 'Section'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['af_documentation.Section']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'djangoplugins.plugin': {
            'Meta': {'ordering': "(u'_order',)", 'unique_together': "(('point', 'name'),)", 'object_name': 'Plugin'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'point': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangoplugins.PluginPoint']"}),
            'pythonpath': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'djangoplugins.pluginpoint': {
            'Meta': {'object_name': 'PluginPoint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pythonpath': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['af_documentation']