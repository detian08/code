# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013-2015 Therp BV (<http://therp.nl>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CKEditor widget',
    'version': '10.0',
    'author': "HashMicro/Vu",
    'website': 'https:HashMicro.com',
    'summary': 'Provides a widget for editing HTML fields using CKEditor 4.x',
    "category": "Tools",
    "depends": [
        'web',
        'web_editor',
    ],
    'data': [
        'views/qweb.xml',
    ],
    'css': [
        'static/src/css/web_ckeditor4.css',
    ],
    'qweb': [
            "static/src/xml/*.xml",
        ],
    'installable': True,
    'auto_install': False,
    'certificate': '',
}