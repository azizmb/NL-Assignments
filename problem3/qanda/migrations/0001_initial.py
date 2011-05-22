# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Question'
        db.create_table('qanda_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posted_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('posted_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('question', self.gf('django.db.models.fields.TextField')(max_length=100)),
        ))
        db.send_create_signal('qanda', ['Question'])

        # Adding model 'Answer'
        db.create_table('qanda_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('posted_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('posted_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['qanda.Question'])),
            ('answer', self.gf('django.db.models.fields.TextField')(max_length=100)),
        ))
        db.send_create_signal('qanda', ['Answer'])


    def backwards(self, orm):
        
        # Deleting model 'Question'
        db.delete_table('qanda_question')

        # Deleting model 'Answer'
        db.delete_table('qanda_answer')


    models = {
        'qanda.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': "orm['qanda.Question']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'qanda.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['qanda']
