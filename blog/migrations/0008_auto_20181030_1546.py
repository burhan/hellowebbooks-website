# Generated by Django 2.1.2 on 2018-10-30 15:46

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181030_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('paragraph', wagtailmarkdown.blocks.MarkdownBlock(icon='code'))]),
        ),
    ]
