# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['SkeletonCrew.py'],
             pathex=['/Users/ldjam/PycharmProjects/SkeletonCrew'],
             binaries=[],
             datas=[("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/backgrounds/level1.png","Assets/backgrounds/"),
             ("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/backgrounds/level2.png","Assets/backgrounds/"),
             ("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/backgrounds/titlescreen.png","Assets/backgrounds/"),
             ("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/backgrounds/winscreen.png","Assets/backgrounds/"),
             ("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/images/desk.png","Assets/images/"),
             ("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/images/plant.png","Assets/images/"),
             ("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/images/player.png","Assets/images/"),
             ("/Users/ldjam/PycharmProjects/SkeletonCrew/Assets/images/watercooler.png","Assets/images/")],
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
          [],
          exclude_binaries=True,
          name='SkeletonCrew',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='SkeletonCrew')
app = BUNDLE(coll,
             Tree('Assets', prefix='Assets'),
             name='SkeletonCrew.app',
             icon=None,
             bundle_identifier=None)
