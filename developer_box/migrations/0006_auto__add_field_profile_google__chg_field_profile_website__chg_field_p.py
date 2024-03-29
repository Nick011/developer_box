# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Item', fields ['slug']
        db.delete_unique(u'developer_box_item', ['slug'])

        # Adding field 'Profile.google'
        db.add_column(u'developer_box_profile', 'google',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)


        # Changing field 'Profile.website'
        db.alter_column(u'developer_box_profile', 'website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Profile.bio'
        db.alter_column(u'developer_box_profile', 'bio', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Profile.github'
        db.alter_column(u'developer_box_profile', 'github', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Profile.twitter'
        db.alter_column(u'developer_box_profile', 'twitter', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Profile.linkedin'
        db.alter_column(u'developer_box_profile', 'linkedin', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Profile.stackoverflow'
        db.alter_column(u'developer_box_profile', 'stackoverflow', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))
        # Deleting field 'Tag.title'
        db.delete_column(u'developer_box_tag', 'title')

        # Adding field 'Tag.name'
        db.add_column(u'developer_box_tag', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Deleting field 'Item.body'
        db.delete_column(u'developer_box_item', 'body')

        # Adding field 'Item.description'
        db.add_column(u'developer_box_item', 'description',
                      self.gf('django.db.models.fields.TextField')(default='test test'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Profile.google'
        db.delete_column(u'developer_box_profile', 'google')


        # Changing field 'Profile.website'
        db.alter_column(u'developer_box_profile', 'website', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Profile.bio'
        db.alter_column(u'developer_box_profile', 'bio', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Profile.github'
        db.alter_column(u'developer_box_profile', 'github', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Profile.twitter'
        db.alter_column(u'developer_box_profile', 'twitter', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Profile.linkedin'
        db.alter_column(u'developer_box_profile', 'linkedin', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Profile.stackoverflow'
        db.alter_column(u'developer_box_profile', 'stackoverflow', self.gf('django.db.models.fields.URLField')(default='', max_length=200))
        # Adding field 'Tag.title'
        db.add_column(u'developer_box_tag', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)

        # Deleting field 'Tag.name'
        db.delete_column(u'developer_box_tag', 'name')

        # Adding field 'Item.body'
        db.add_column(u'developer_box_item', 'body',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Item.description'
        db.delete_column(u'developer_box_item', 'description')

        # Adding unique constraint on 'Item', fields ['slug']
        db.create_unique(u'developer_box_item', ['slug'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'developer_box.bucket': {
            'Meta': {'object_name': 'Bucket'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['developer_box.Item']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'developer_box.comment': {
            'Meta': {'object_name': 'Comment'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'developer_box.item': {
            'Meta': {'object_name': 'Item'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'last_viewed_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'script': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['developer_box.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'developer_box.profile': {
            'Meta': {'object_name': 'Profile'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'google': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'stackoverflow': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        'developer_box.tag': {
            'Meta': {'object_name': 'Tag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_used_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['developer_box']