# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table('socialcomments_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('provider', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('identity', self.gf('django.db.models.fields.EmailField')(max_length=255, db_index=True)),
            ('sent', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('spam', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('socialcomments', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table('socialcomments_comment')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'socialcomments.comment': {
            'Meta': {'ordering': "('-sent',)", 'object_name': 'Comment'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'spam': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['socialcomments']