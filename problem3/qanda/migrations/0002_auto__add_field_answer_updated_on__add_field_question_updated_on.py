# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Answer.updated_on'
        db.add_column('qanda_answer', 'updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 5, 21), blank=True), keep_default=False)

        # Adding field 'Question.updated_on'
        db.add_column('qanda_question', 'updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 5, 21), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Answer.updated_on'
        db.delete_column('qanda_answer', 'updated_on')

        # Deleting field 'Question.updated_on'
        db.delete_column('qanda_question', 'updated_on')


    models = {
        'qanda.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': "orm['qanda.Question']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'qanda.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['qanda']
