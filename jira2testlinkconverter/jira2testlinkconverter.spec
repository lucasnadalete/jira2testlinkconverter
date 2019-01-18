# -*- mode: python -*-

block_cipher = None


a = Analysis(['jira2testlinkconverter.py'],
             pathex=['/home/lnadalete/Documents/Tools/Testlink/jira2testlinkexporter'],
             binaries=[],
             datas=[('./templates/*.xml', './templates')],
             hiddenimports=[],
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
          name='jira2testlinkconverter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
