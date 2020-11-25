# -*- mode: python ; coding: utf-8 -*-

import PyInstaller
import spacy

block_cipher = None


datas = []
datas.extend(PyInstaller.utils.hooks.collect_data_files('spacy.lang', include_py_files = True))
# datas.extend(PyInstaller.utils.hooks.collect_data_files('spacy_lookups_data'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('en_core_web_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('thinc'))
datas.append((spacy.util.get_data_path(), 'spacy/data'))
hiddenimports = [
    'spacy.kb',
    'spacy.lexeme',
    'spacy.matcher._schemas',
    'spacy.morphology',
    'spacy.parts_of_speech',
    'spacy.syntax._beam_utils',
    'spacy.syntax._parser_model',
    'spacy.syntax.arc_eager',
    'spacy.syntax.ner',
    'spacy.syntax.nn_parser',
    'spacy.syntax.stateclass',
    'spacy.syntax.transition_system',
    'spacy.tokens._retokenize',
    'spacy.tokens.morphanalysis',
    'spacy.tokens.underscore',

    'blis',
    'blis.py',

    'cymem',
    'cymem.cymem',

    'murmurhash',

    'preshed.maps',

    'srsly.msgpack.util',

    'thinc.extra.search',
    'thinc.linalg',
    'thinc.neural._aligned_alloc',
    'thinc.neural._custom_kernels'
]

a = Analysis(['main.py'],
             pathex=['C:\\development\\extraction'],
             binaries=[],
             datas=datas,
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )