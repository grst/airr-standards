#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# airr-standards documentation build configuration file, created by
# sphinx-quickstart on Fri Nov 17 14:47:21 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- Imports ----------------------------------------------------------------

import csv
import os
import sys
import yaml
import yamlordereddictloader
from unittest.mock import MagicMock

# -- Python environment ----------------------------------------------------

# Python system path
sys.path.append(os.path.abspath('.'))

# Mock modules for ReadTheDocs
if os.environ.get('READTHEDOCS', None) == 'True':
    class Mock(MagicMock):
        @classmethod
        def __getattr__(cls, name):  return MagicMock()

    mock_modules = ['numpy', 'pandas']
    sys.modules.update((mod_name, Mock()) for mod_name in mock_modules)

# -- General configuration ------------------------------------------------

# Setup
# def setup(app):
#     # Can also be a full URL
#     app.add_stylesheet('submenus.css')
#     app.add_stylesheet("overrides.css")

rst_prolog ='''
.. |br| raw:: html

   <br />
'''

# Minimal Sphinx version
needs_sphinx = '1.6'

# Sphinx extension modules
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinxcontrib.autoprogram',
              'rstjinjaext']

# Define source file extensions
source_suffix = ['.rst']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'AIRR Standards'
copyright = '2017-2020, AIRR Community'
author = 'AIRR Community'

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = 'bash'
pygments_style = 'vs'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# HTML help
htmlhelp_basename = 'airr-standardsdoc'

# Alabaster options
# html_theme = 'alabaster'
# html_theme_options = {'github_user': 'airr-community',
#                       'github_repo': 'airr-standards',
#                       'github_button': True,
#                       'sidebar_includehidden': True,
#                       'sidebar_width': '300px',
#                       'extra_nav_links': {'AIRR Community': 'http://airr-community.org'}}
# html_sidebars = {'**': ['about.html',
#                         'navigation.html',
#                         'searchbox.html']}

# PyData options
# html_theme = "pydata_sphinx_theme"
html_theme = "sphinx_book_theme"
html_logo = "_static/AIRR_logo-only.png"

# Bootstrap options
# html_theme = 'bootstrap'
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
# html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}
# html_sidebars = {'**': ['globaltoc.html']}
# html_sidebars = {'**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html']}
# html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}
# html_theme_options = {
#     # Navigation bar title. (Default: ``project`` value)
#     'navbar_title': 'AIRR Community Standards',
#
#     # Tab name for entire site. (Default: "Site")
#     'navbar_site_name': 'Contents',
#
#     # A list of tuples containing pages or urls to link to.
#     # Valid tuples should be in the following forms:
#     #    (name, page)                 # a link to a page
#     #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
#     #    (name, "http://example.com", True) # arbitrary absolute url
#     # Note the "1" or "True" value above as the third argument to indicate
#     # an arbitrary url.
#     # 'navbar_links': [('GitHub', 'https://github.com/airr-community/airr-standards', True),
#     #                  ('AIRR-C', 'http://airr-community.org', True)],
#
#     # Render the next and previous page links in navbar. (Default: true)
#     'navbar_sidebarrel': True,
#
#     # Render the current pages TOC in the navbar. (Default: true)
#     'navbar_pagenav': True,
#
#     # Tab name for the current pages TOC. (Default: "Page")
#     'navbar_pagenav_name': 'Page',
#
#     # Global TOC depth for "site" navbar tab. (Default: 1)
#     # Switching to -1 shows all levels.
#     'globaltoc_depth': 1,
#
#     # Include hidden TOCs in Site navbar?
#     #
#     # Note: If this is "false", you cannot have mixed ``:hidden:`` and
#     # non-hidden ``toctree`` directives in the same page, or else the build
#     # will break.
#     #
#     # Values: "true" (default) or "false"
#     'globaltoc_includehidden': 'false',
#
#     # HTML navbar class (Default: "navbar") to attach to <div> element.
#     # For black navbar, do "navbar navbar-inverse"
#     'navbar_class': 'navbar',
#
#     # Fix navigation bar to top of page?
#     # Values: "true" (default) or "false"
#     'navbar_fixed_top': 'true',
#
#     # Location of link to source.
#     # Options are "nav" (default), "footer" or anything else to exclude.
#     'source_link_position': 'none',
#
#     # Bootswatch (http://bootswatch.com/) theme.
#     #
#     # Options are nothing (default) or the name of a valid theme
#     # such as "cosmo" or "sandstone".
#     #
#     # The set of valid themes depend on the version of Bootstrap
#     # that's used (the next config option).
#     #
#     # Currently, the supported themes are:
#     # - Bootstrap 2: https://bootswatch.com/2
#     # - Bootstrap 3: https://bootswatch.com/3
#     'bootswatch_theme': 'spacelab',
#
#     # Choose Bootstrap version.
#     # Values: "3" (default) or "2" (in quotes)
#     'bootstrap_version': '2',
# }

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'airr-standards.tex', 'airr-standards Documentation',
     'AIRR Community', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'airr-standards', 'airr-standards Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'airr-standards', 'airr-standards Documentation',
     author, 'airr-standards', 'One line description of project.',
     'Miscellaneous'),
]

# -- Build schema reference tables ----------------------------------------

# Function to chop down long strings of the table
def wrap_col(string, str_length=11):
    """
    String wrap
    """
    if [x for x in string.split(' ') if len(x) > 25]:
        parts = [string[i:i + str_length].strip() for i in range(0, len(string), str_length)]
        return ('\n'.join(parts) + '\n')
    else:
        return (string)

def parse_schema(spec, schema):
    """
    Parse an AIRR schema object for doc tables

    Arguments:
      spec (str): name of the schema object
      schema (dict): master schema dictionary parsed from the yaml file.

    Returns:
      list: list of dictionaries with parsed rows of the spec table.
    """
    data_type_map = {'string': 'free text',
                     'integer': 'positive integer',
                     'number': 'positive number',
                     'boolean': 'true | false'}

    # Get schema
    properties = schema[spec]['properties']
    required = schema[spec].get('required', None)

    # Iterate over properties
    table_rows = []
    for prop, attr in properties.items():
        # Standard attributes
        required_field = False if required is None or prop not in required else True
        title = attr.get('title', '')
        example = attr.get('example', '')
        description = attr.get('description', '')

        # Data type
        data_type = attr.get('type', '')
        data_format = data_type_map.get(data_type, '')

        # Arrays
        if data_type == 'array':
            if attr['items'].get('$ref') is not None:
                sn = attr['items'].get('$ref').split('/')[-1]
                data_type = 'array of :ref:`%s <%sFields>`' % (sn, sn)
            elif attr['items'].get('type') is not None:
                data_type = 'array of %s' % attr['items']['type']
        elif attr.get('$ref') == '#/Ontology':
            data_type = ':ref:`Ontology <OntoVoc>`'
        elif attr.get('$ref') is not None:
            sn = attr.get('$ref').split('/')[-1]
            data_type = ':ref:`%s <%sFields>`' % (sn, sn)

        # x-airr attributes
        if 'x-airr' in attr:
            xairr = attr['x-airr']
            nullable = xairr.get('nullable', True)
            deprecated = xairr.get('deprecated', False)
            identifier = xairr.get('identifier', False)

            # MiAIRR attributes
            miairr_level = xairr.get('miairr', '')
            miairr_set = xairr.get('set', '')
            miairr_subset = xairr.get('subset', '')

            # Set data format for ontologies and controlled vocabularies
            if 'format' in xairr:
                if xairr['format'] == 'ontology' and 'ontology' in xairr:
                    base_dic = xairr['ontology']
                    ontology_format = (str(base_dic['top_node']['id']), str(base_dic['top_node']['label']) )
                    # Replace name with url-linked name
                    data_format = 'Ontology: { top_node: { id: %s, value: %s}}' % (ontology_format)
                    # Get 'type' for ontology
                    example = 'id: %s, value: %s' % (example['id'], example['label'])
                elif xairr['format'] == 'controlled vocabulary':
                    if attr.get('enum', None) is not None:
                        data_format = 'Controlled vocabulary: %s' % ', '.join(attr['enum'])
                    elif attr.get('items', None) is not None:
                        data_format = 'Controlled vocabulary: %s' % ', '.join(attr['items']['enum'])
        else:
            nullable = True
            deprecated = False
            identifier = False
            miairr_level = ''
            miairr_set = ''
            miairr_subset = ''

        if deprecated:
            field_attributes = 'DEPRECATED'
        else:
            f = ['required' if required_field else 'optional',
                 'identifier' if identifier else '',
                 'nullable' if nullable else '']
            field_attributes = ', '.join(filter(lambda x: x != '', f))

        # Return dictionary
        r = {'Name': prop,
             'Set': miairr_set,
             'Subset': miairr_subset,
             'Designation': title,
             'Field': prop,
             'Type': data_type,
             'Format': data_format,
             'Definition': description,
             'Example': example,
             'Level': miairr_level,
             'Required': required_field,
             'Deprecated': deprecated,
             'Nullable': nullable,
             'Identifier': identifier,
             'Attributes': field_attributes}

        table_rows.append(r)

    return(table_rows)

# Load data for schemas
with open(os.path.abspath('../specs/airr-schema.yaml')) as ip:
    airr_schema = yaml.load(ip, Loader=yamlordereddictloader.Loader)
html_context = {'airr_schema': airr_schema}

# Iterate over schema and build reference tables
data_elements = {}
for spec in airr_schema:
    if 'properties' not in airr_schema[spec]:
        continue

    # Storage object
    data_elements[spec] = parse_schema(spec, airr_schema)

    # Update doc html_context
    html_context[spec + '_schema'] = data_elements[spec]

# -- Write download tables ------------------------------------------------

# Write download spec files
download_path = '_downloads'
if not os.path.exists(download_path):  os.mkdir(download_path)

# Write MiAIRR TSV
fields = ['Set', 'Subset', 'Designation', 'Field', 'Type', 'Format', 'Level', 'Definition', 'Example']
tables = ['Study', 'Subject', 'Diagnosis', 'Sample', 'CellProcessing', 'NucleicAcidProcessing',
          'PCRTarget', 'SequencingRun', 'RawSequenceData', 'DataProcessing']
# tables = data_elements.keys()
miairr_schema = []
with open(os.path.join(download_path, '%s.tsv' % 'AIRR_Minimal_Standard_Data_Elements'), 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fields, dialect='excel-tab', extrasaction='ignore')
    writer.writeheader()
    for spec in tables:
        for r in data_elements[spec]:
            if r['Level'] and not r['Deprecated']:
                miairr_schema.append(r)
                writer.writerow(r)
html_context['MiAIRR_schema'] = miairr_schema

# Write individual spec TSVs
fields = ['Name', 'Type', 'Attributes', 'Definition']
tables = ['Repertoire', 'Study', 'Subject', 'Diagnosis', 'Sample', 'CellProcessing', 'NucleicAcidProcessing',
          'PCRTarget', 'SequencingRun', 'RawSequenceData', 'DataProcessing',
          'Rearrangement', 'Alignment', 'Clone', 'Tree', 'Node', 'Cell',
          'RearrangedSequence', 'GermlineSequence', 'GeneDelineationV', 'GeneDescription', 'GermlineSet']
for spec in tables:
    with open(os.path.join(download_path, '%s.tsv' % spec), 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fields, dialect='excel-tab', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data_elements[spec])

# -- Site configuration from schema data ----------------------------------

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = str(airr_schema['Info']['version'])
# The full version, including alpha/beta/rc tags.
release = str(airr_schema['Info']['version'])
