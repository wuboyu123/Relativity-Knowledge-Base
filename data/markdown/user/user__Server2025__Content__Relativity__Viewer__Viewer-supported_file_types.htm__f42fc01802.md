---
title: "Viewer-supported file types"
url: https://help.relativity.com/Server2025/Content/Relativity/Viewer/Viewer-supported_file_types.htm
collection: user
fetched_at: 2026-06-22T06:16:46+00:00
sha256: f8fb86e0a5af3a0d7ae2c840a7629e4ba0a0c2bcd4cef335f99e27936d0b0ace
---

Viewer-supported file types

# Viewer-supported file types

Relativity uses the Viewer to display rendered versions of native files. Reviewers can see how the file looked in its native application without opening the file in that native application.

When converting email file types such as EML, the Viewer will not download images from the internet. Any linked images will display as a gray box in the Viewer.

This page provides a comprehensive list of files types supported by the Viewer. Find out which Viewer version you have, by navigating to your Viewer and clicking . For more information, see Viewer .

Relativity does not support any third-party applications after the user downloads a file. This includes specific browser and media-player combinations, such as Internet Explorer and Windows Media Player.

Supported file types differ slightly in processing, imaging, and the Viewer. You can use the following links to see the differences in processing and imaging:

- Supported file types for processing

- Supported file types for imaging

## Text only designation

Some file types have a "text only" designation. When viewing these files in the Native Viewer, the document's text is the only data that renders. For Microsoft Project files and XML files, the view doesn't display items such as Gantt charts, icons, or other graphics. There is typically no formatting (bold, italics, fonts, etc.) of the text.

## File ID only designation

Some file types have a "file ID only" designation. The Viewer is able to identify the file ID correctly, but it returns an error message indicating that the file format is not supported. Despite returning an error message, the Viewer identifies the file so that you can easily locate it and open it in an alternate application.

## Supported File ID-only file types

The Viewer supports file ID-only functionality the following native file types. The supported file types are listed by category.

Program/File Type Category Type/Version File Extension

Microsoft Access Report Snapshot Database 2000-2003

IBM Lotus Notes NSF Email 7.x, 8.x

DICOM Multimedia

Flash Multimedia 9, 10

Real Media Multimedia

MPEG-1 Video V 2 Multimedia .mpg

MPEG-1 Video V 3 Multimedia .mpg

MPEG-2 Audio Multimedia .mpg

Windows Media Playlist Multimedia

AOL Messenger Other

Microsoft InfoPath Other 2007

Microsoft Office Theme files Other 2007-2013

Microsoft Windows Compiled Help Other .chm

Microsoft Windows Explorer Command Other .scf

Microsoft Windows Help Other .hlp

Microsoft Windows Shortcut Other .ink

Trillian XML Log File Other 4.2

Adobe Photoshop PSD Raster

TrueType Font Other .ttf, .ttc

WebP Raster

XHTML Text and Markup 1.0

Visio XML VSX Vector Image 2007

Microsoft Publisher Word Processing 2003-2007

Samsung JungUm Global Word Processing

Strict Open XML - Presentation

Relativity does not support the password protected version for these three Strict Open XML file formats.

Presentation 2013, 2016

Strict Open XML - Spreadsheet Spreadsheet 2013, 2016

Strict Open XML - Document Word Processing 2013, 2016

## Supported Text-only file types

The Viewer supports text-only functionality the following native file types. The supported file types are listed by category.

Program/File Type Category Type/Version File Extension

Microsoft Access Database 1.0, 2.0, 95 - 2010 .accdb, .mdb

Flash Multimedia 6.x, 7.x, Lite .swf

Microsoft Excel for Windows Spreadsheet 2003 XML .xml

XML Text and markup .xml

Microsoft XPS Vector Image

Visio Vector Image 2013

Lotus WordPro Word processing 9.7, 96 - Millennium 9.8 .lwp, .mwp

Microsoft Word for Windows Word Processing 2003 XML

## Supported File types

The Viewer supports the following native file types. The supported file types are listed by category.

Program/File Type Category Type/Version File Extension

7z

Note : BZIP2 and split archives are not supported.

Archive .7z

7z Self Extracting exe

Note : BZIP2 and split archives are not supported.

Archive .exe

LZA Self Extracting Compress Archive .lza

LZH Compress Archive .lzh

Microsoft Office Binder Archive 95, 97 .obd

Microsoft Cabinet (CAB) Archive .cab

PKZip Archive .zip

RAR Archive 1.5, 2.0, 2.9 .rar

UNIX Compress Archive .z

UNIX GZip Archive .gz

UNIX tar Archive .tar

Uuencode Archive .uue

Zip Archive PKZip, WinZip .zip

DataEase Database 4.x .dba

DBase Database III, IV, V .dbf

First Choice DB Database Through 3.0 .fol

Framework DB Database 3.0

Microsoft Access Database 2007/2010 .accdb

Microsoft Works DB for DOS Database 2.0 .wdb

Microsoft Works DB for Macintosh Database 2.0 .wdb

Microsoft Works DB for Windows Database 3.0, 4.0 .wdb

Microsoft Works DB for DOS Database 1.0 .wdb

Paradox for DOS Database 2.0 - 4.0 .db

Paradox for Windows Database 1.0 .db

Q&A Database Database Through 2.0 .db

R:Base Database R:Base 5000, R:Base System V .rb1, .rb2, .rb3

Reflex Database 2.0 .rdx

SmartWare II DB Database 1.02 .db

Apple Mail Message (EMLX) Email 2.0 .emlx

Encoded mail messages Email

- MHT

- Multi Part Alternative

- Multi Part Digest

- Multi Part Mixed

- Multi Part News Group

- Multi Part Signed

- TNEF

EML with Digital Signature

.EML files that have a password or are encrypted are not supported in the Viewer. These documents will display the attachment but the body will appear blank.

Email SMIME .eml

IBM Lotus Notes Domino XML Language DXL Email 8.5 .xml

IBM Lotus Notes NSF (Win32, Win64, Linux x86-32 and Oracle Solaris 32-bit only with Notes Client or Domino Server) Email 8.x .nsf. .ntf

MBOX Mailbox

Any MBOX file that is ingested into Relativity using the Relativity Desktop Client will display as an archive, regardless of how many messages it may have or what extension it might have. An MBOX file is characterized as a text file with the string "From<space>email address<space>date string". When a file of this nature is viewed in Relativity, it may appear to only show summaries of messages. Essentially, if that "from" line is at the top of the document, Relativity treats it as MBOX and displays it as an archive.

Email RFC 822 .mbox

Microsoft Outlook (MSG) Email 97 - 2013 .msg

Microsoft Outlook (OST ) Email 97 - 2010, 2013 .ost

Microsoft Outlook (PST) Email 97 - 2013 .pst

Microsoft Outlook Express (EML) Email .eml

Microsoft Outlook Forms Template (OFT) Email 97 - 2013 .oft

Microsoft Outlook OLM for Mac Email 2011

Microsoft Outlook PST (Mac) Email 2001 .pst

MSG with Digital Signature

.MSG files that have a password or are encrypted are not supported in the Viewer. If you open an .MSG file that is encrypted in the Viewer, the body of the document will be blank and the contents of the encrypted data is placed into a single attachment with a .p7m file extension.

Email SMIME .msg

Microsoft Live Messenger (via XML filter) Other 10.0

Microsoft OneNote

The Viewer does not support OneNote files with the Relativity Native type: Microsoft OneNote SOAP/HTTP File.

Other 2007, 2010, 2013 .one

Microsoft Outlook, Google Calendar, and Apple Calendar Other .ics

Microsoft Project (sheet view only, Gantt Chart, Network Diagram, and graph not supported) Other 98-2013 .mpp

Microsoft Project (sheet view only, Gantt Chart, Network Diagram, and graph not supported) Other 2007, 2010, 2013 .mpp

Microsoft Windows DLL Other .dll

Microsoft Windows Executable Other .dll

Trillian Text Log File (via text filter) Other 4.2 .txt

vCalendar Other 2.1 .vcs

vCard Other 2.1 .vcf

Yahoo! Messenger Other 6.x – 8 .yps

Apache Office Draw (ODF 1.2) Presentation 3.x, 4.x

Apache Office Impress (ODF 1.2) Presentation 3.x, 4.x

Apple iWork Keynote (MacOS, text and PDF preview) Presentation 09 .key, .keynote

Harvard Graphics Presentation DOS Presentation 3.0 .prs

IBM Lotus Symphony Presentations Presentation 1.x

Kingsoft WPS Presentation Presentation 2010

Libre Office Draw (ODF 1.2) Presentation 3.x, 4.x

Libre Office Impress (ODF 1.2) Presentation 3.x, 4.x

Lotus Freelance Presentation 1.0 - Millennium 9.8 .prz

Lotus Freelance for OS/3 Presentation 2

Lotus Freelance for Windows Presentation 95, 97, SmartSuite 9.8

Microsoft PowerPoint for Macintosh Presentation 4.0 - 2011 .ppt

Microsoft PowerPoint for Windows Presentation 3.0 – 2013 .ppt

Microsoft PowerPoint 2016

.pptx files that have Ink drawings are supported in the Native and Image Viewer.

Presentation 2016 .pptx

Microsoft PowerPoint for Windows Slideshow Presentation 2007-2013 .ppt

Microsoft PowerPoint for Windows Template Presentation 2007-2013 .pot

Novell Presentations Presentation 3.0, 7.0 .shw

OpenOffice Impress Presentation 1.1, 3.0 .sdd

Oracle Open Office Impress Presentation 3.x .odp

StarOffice Impress Presentation 5.2 - 9.0 .sda, .sdd

WordPerfect Presentations Presentation 5.1 - X5

Adobe Photoshop Raster image 4.0 .psd

Adobe Photoshop XMP only Raster image 8.0 - 10.0 (CS 1-5)

CALS Raster (GP4) Raster image Type I-II .cg4, .cal

Computer Graphics Metafile Raster image ANSI, CALS, NIST .cgm

Encapsulated PostScript (EPS) Raster image TIFF Header only .eps

GEM Image (Bitmap) Raster image .bmp

Graphics Interchange Format (GIF) Raster image .gif

IBM Graphics Data Format (GDF) Raster image 1.0 .gdf

IBM Picture Interchange Format Raster image 1.0 .pif

HEIC Image file Raster image .heic

JBIG2 Raster image Graphic Embeddings in PDF

JFIF (JPEG not in TIFF format) Raster image .jfif

JPEG Raster image .jpg

JPEG 2000 Raster image JP2

Kodak Flash Pix Raster image .fpx

Kodak Photo CD Raster image 1.0 .pcd

Lotus PIC Raster image .pic

Lotus Snapshot Raster image

Macintosh PICT Raster image BMP only .bmp

Macintosh PICT2 Raster image BMP only .bmp

MacPaint Raster image .pntg

Microsoft Windows Bitmap Raster image .bmp

Microsoft Windows Cursor Raster image

Microsoft Windows Icon Raster image .ico

OS/2 Bitmap Raster image

OS/2 Warp Bitmap Raster image

Paint Shop Pro (Win32 only) Raster image 5.0, 6.0 .psp

PC Paintbrush (PCX) Raster image .pcx

PC Paintbrush DCX (multi-page PCX) Raster image .dcx

Portable Bitmap (PBM) Raster image .pbm

Portable Graymap PGM Raster image .pgm

Portable Network Graphics (PNG) Raster image .png

Portable Pixmap (PPM) Raster image .ppm

Progressive JPEG Raster image .jpg, .jpeg, .jpe

StarOffice Draw Raster image 6.x - 9.0

Sun Raster Raster image .srs

TIFF Raster image Group 5 & 6 .tif, .tiff

TIFF CCITT Raster image Group 3 & 4

TruVision TGA (Targa) Raster image 2.0 .tga

WBMP wireless graphics format Raster image

Word Perfect Graphics Raster image 1.0 .wpg

WordPerfect Graphics Raster image 2.0 – 10.0 .wpg, .wpg2

X-Windows Bitmap Raster image x10 compatible .xbm

X-Windows Dump Raster image x10 compatible .xdm

X-Windows Pixmap Raster image x10 compatible .xpm

Apache Office Calc (ODF 1.2) Spreadsheet 3.x, 4.x

Apple iWork Numbers (MacOS, text, and PDF preview) Spreadsheet 09 .numbers

Enable Spreadsheet Spreadsheet 3.0 - 4.5

First Choice SS Spreadsheet Through 3.0

Framework SS Spreadsheet 3.0

IBM Lotus Symphony Spreadsheets Spreadsheet 1.x

Kingsoft WPS Spreadsheets Spreadsheet 2010

Libre Office Calc (ODF 1.2) Spreadsheet 3.x, 4.x

Lotus 1-2-3 Spreadsheet Through Millennium 9.8 .wk1, .wk3, .wk4, .wks

Lotus 1-2-3 Charts (DOS and Windows) Spreadsheet Through 5.0 .wk1, .wk3, .wk4, .wks

Lotus 1-2-3 for OS/2 Spreadsheet 2.0

Microsoft Excel Charts Spreadsheet 2.x - 2007 .xlsx, .xls

Microsoft Excel for Macintosh Spreadsheet 98 – 2011 .xlsx, .xls

Microsoft Excel for Windows

Excel files with slicers will convert and display normally in the Viewer, but slicer elements in those files will not display.

Spreadsheet 3.0 - 2016 .xlsx, .xls

Microsoft Excel for Windows (.xlsb) Spreadsheet 2007-2013 (Binary) .xlsb

Microsoft Works SS for DOS Spreadsheet 2.0 .wks

Microsoft Works SS for Macintosh Spreadsheet 2.0 .wks

Microsoft Works SS for Windows Spreadsheet 3.0, 4.0 .wks

Multiplan Spreadsheet 4.0 .sylk

Novell PerfectWorks Spreadsheet Spreadsheet 2.0 .wpw

OpenOffice Calc Spreadsheet 1.1-3.0 .sdc

Oracle Open Office Calc Spreasheet 3.x .sdc

Office Calc (ODF 1.2) Spreadsheet 4.x

PFS: Plan Spreadsheet 1.0

QuattroPro for DOS Spreadsheet Through 5.0 .wb1

QuattroPro for Windows Spreadsheet Through X5 .qpw, .wb3, .wb2, .wb1

Quattro Pro Win Spreadsheet X7 .qpw

SmartWare II SS Spreadsheet 1.02 .def

SmartWare Spreadsheet Spreadsheet .def

StarOffice Calc Spreadsheet 5.2 – 9.0 .sdc

SuperCalc Spreadsheet 5.0 .cal

Symphony Spreadsheet Through 2.0 .wrk

VP-Planner Spreadsheet 1.0

ANSI Text Text and markup 7 & 8 bit .ans

ASCII Text Text and markup 7 & 8 bit .asc

DOS character set Text and markup

EBCDIC Text and markup

HTML (CSS rendering not supported) Text and markup 1.0 – 4.0 .html

IBM DCA/RFT Text and markup

Macintosh character set Text and markup

Rich Text Format (RTF) Text and markup .rtf

Unicode Text Text and markup 3.0, 4.0 .txt

UTF-8 Text and markup

Wireless Markup Language Text and markup .wml

Adobe Illustrator XMP Vector image 11 – 13 (CS 1 - 5)

Adobe InDesign XMP Vector image 3.0 – 5.0 (CS 1 - 5)

Adobe InDesign Interchange XMP only Vector image

Adobe PDF Vector image 1.0 – 1.7 (Acrobat 1 - 10) .pdf

Adobe PDF Package Vector image 1.7 (Acrobat 8 - 10) .pdf

Adobe PDF Portfolio Vector image 1.7 (Acrobat 8 - 10) .pdf

Ami Draw Vector image SDW .sdw

Apple iWork Keynote File Preview Vector 09 .key, .keynote

Apple iWork Keynote Numbers File Preview Vector 09 .numbers

Apple iWork Pages File Preview Vector 09 .pages

AutoCAD Drawing Vector image 2.5, 2.6, 9.0-14.0, 2000i -2012 .dwg

AutoCAD Drawing Vector 2013 .dwg

AutoShade Rendering Vector image 2 .rnd

Corel Draw Vector image X4 - X7 .cdr

Corel Draw Clipart Vector image 5.0, 7.0 .cmx

Enhanced Metafile (EMF) Vector image .emf

Escher Graphics Vector image .egr

FrameMaker Graphics (FMV) Vector image 3.0 – 5.0 .fmv

Gem File (Vector) Vector image .img

Harvard Graphics Vector 98 .cht

Harvard Graphics Chart DOS Vector image 2.0 – 3.0 .ch3

Harvard Graphics for Windows Vector image .prs

HP Graphics Language Vector image 2.0 .hp, .hpg

IGES Drawing Vector image 5.1 – 5.3 .iges

Micrografx Designer Vector image Version 6 .dsf

Micrografx Designer Vector image Through 3.1 .drw

Micrografx Draw Vector image Through 4.0 .drw

Novell PerfectWorks Draw Vector image 2.0

OpenOffice Draw Vector image 1.1 – 3.0 .sda

Oracle Open Office Draw Vector image 3.x .sda

SVG (processed as XML, not rendered) Vector image .xml

Microsoft Visio:

- Stencil

- Template

- Macro Enabled Drawing

- Macro Enabled Stencil

- Macro Enabled Template

Vector image 5.0 – 2007, 2013 .vsd

Visio (Page Preview mode WMF/EMF) Vector image 4.0 .wmf, .emf

Windows Metafile Vector image .vmf

Adobe FrameMaker (MIF only) Word processing 3.0 - 6.0 .mif

Adobe Illustrator Postscript Word processing Level 2 .eps

Ami Word processing

Ami Pro for OS2 Word processing .sam

Ami Pro for Windows Word processing 2.0, 3.0 .sam

Apache Office Writer (ODF 1.2) Word processer 3.x, 4.x

Apple iWork Pages (MacOS, text and PDF preview) Word processing 09 .pages

DEC DX Word processing Through 4.0 .dx

DEC DX Plus Word processing 4.0, 4.1 .dx, .wpl

Enable Word Processor Word processing 3.0 - 4.5

First Choice WP Word processing 1.0, 3.0 .pfx

Framework WP Word processing 3.0

Hangul Word processing 97 - 2010 .hwp

IBM DCA/FFT Word processing .dca, .fft

IBM DisplayWrite Word processing 2.0-5.0 .rft, .dca

IBM Writing Assistant Word processing 1.01 .iwa

Ichitaro Word processing 5.0, 6.0, 8.0 - 13.x, 2004 - 2014 .jtd

JustWrite Word processing Through 3.0 .jw

Kingsoft WPS Writer Word processing 2010 .wps

Legacy Word processing 1.1 .leg

Libre Office Writer (ODF 1.2) Word processor 3.x, 4.x

Lotus Manuscript Word processing Through 2.0 .manu

MacWrite II Word processing 1.1 .mcw

Mail Rule DXL Word processing

Mass 11 Word processing Through 8.0 .m11

Microsoft Word for DOS Word processing 4.0 – 6.0 .doc

Microsoft Word for Macintosh Word processing 4.0-6.0, 98 - 2016 .doc

Microsoft Word for Windows Word processing 1.0 – 2016 .doc, .docx

Microsoft WordPad Word processing .rtf

Microsoft Works WP for DOS Word processing 2.0 .wps

Microsoft Works WP for Macintosh Word processing 2.0 .wps

Microsoft Works WP for Windows Word processing 3.0, 4.0 .wps

Microsoft Write for Windows Word processing 1.0 – 3.0 .wri

MultiMate Word processing Through 4.0 .dox

MultiMate Advantage Word processing 2.0 .dox

Navy DIF Word processing .dif

Nota Bene Word processing 3.0 .nb

Novell PerfectWorks Word Processor Word processing 2.0 .wpw

OfficeWriter Word processing 4.0-6.0

OpenOffice Writer Word processing 1.1 - 3.0 .sdw

Oracle Open Office Writer Word processing 3.x .sdw

PC File Doc Word processing 5.0

PFS: Write Word processing A, B .pfs

Professional Write for DOS Word processing 1.0, 2.0

Professional Write Plus for Windows Word processing 1.0

Q&A Write Word processing 2.0, 3.0 .jw

Samna Word IV Word processing 1.0 – 3.0 .sam

Samna Word IV+ Word processing .sam

Signature Word processing 1.0

SmartWare II WP Word processing 1.02 .def

Sprint Word processing 1.0 .spr

StarOffice Writer Word processing 5.2 – 9.0 .sdw

Total Word Word processing 1.2

Wang IWP Word processing Through 2.6 .iwp

WordMarc Composer Word processing

WordMarc Composer+ Word processing

WordMarc Word Processor Word processing

WordPerfect for DOS Word processing 4.2 .wpd

WordPerfect for Macintosh Word processing 1.02 - 3.1 .wpd

WordPerfect for Windows Word processing 5.1 – X5 .wpd

Wordstar 2000 for DOS Word processing 1.0 - 3.0 .wsd

Wordstar for DOS Word processing 3.0 - 7.0 (none defined)

Wordstar for Windows Word processing 1.0 .ws1

XyWrite Word processing Through III+ .xy

Program/file types listed with text only or PDF preview only can be reviewed in the Viewer as listed. If PDF preview only, a PDF file saved as part of the native will be viewed. Text only will just display the text without any formatting.

## Viewer audio and video-supported file types

Relativity can stream audio and video files within the Viewer.

This page provides a comprehensive list of files types supported by the Viewer. Certain file types may not be compatible with your internet browser, refer to the sections below to learn more about browser compatibility. Find out which Viewer version you have, by navigating to your Viewer and clicking . For more information, see Viewer .

Relativity does not support any third-party applications after the user downloads a file. This includes specific browser and media-player combinations, such as Internet Explorer and Windows Media Player.

## Troubleshooting errors

If an audio or video file cannot be streamed in the Viewer, one of the following messages will display:

To resolve the error, ensure that your internet browser can play the selected file type. If that does not resolve the error, check the MaximumNativeSizeForViewerForMediaFilesinMegaBytes instance setting to ensure that the file type is not too big for the Viewer to stream.

## Supported audio file types

Safari works with Mac OSX only.

File Format Container - Audio Codec Chrome Edge Firefox Safari

FI_RIFFWAVE wave - pcm √ √ √

Quicktime Movie mov - aac √ √ √ √

Quicktime Movie mov - vorbis √ √

MPEG Layer3 ID3 Ver 1.x mp3 - mp3 √ √ √

MPEG Layer3 ID3 Ver 2.x mp3 - mp3 √ √ √ √

FI_MPGAV2L3 mp3 - mp3 √ √ √

MPEG-4 file mp4 - aac √ √ √ √

MPEG-4 file mp4 - opus √ √

MPEG-4 file mp4 - vorbis √ √

MPEG-1 audio - Layer 3 mov - mp3 √ √ √ √

MPEG-1 audio - Layer 2 mp4 - mp2 √ √ √

MPEG-1 audio - Layer 3 mp4 - mp3 √ √ √

Ogg Opus ogg - opus √ √ √

Ogg Vorbis ogg - vorbis √ √ √

## Supported video file types

Safari works with Mac OSX only.

File Format Container - Video Codec - Audio Codec Chrome Edge Firefox Safari

Quicktime Movie mov - h264 - aac √ √ √

Quicktime Movie mov - h264 - dolby_digital √ √ √

Quicktime Movie mov - h264 - mp2 √ √ Video-only

Quicktime Movie mov - h264 - mp3 √ √ √ √

Quicktime Movie mov - h264 - vorbis √ √ √

Quicktime Movie mov - h264 - wma1 √ √ √

Quicktime Movie mov - h264 - wma2 √ √ √

Quicktime Movie mov - mpeg4 - aac Audio-only Audio-only Audio-only √

Quicktime Movie mov - mpeg4 - mp3 Audio-only Audio-only Audio-only

Quicktime Movie mov - mpeg4 - vorbis Audio-only Audio-only √

Quicktime Movie mov - theora - aac √ √ Audio-only

Quicktime Movie mov - theora - dolby_digital √ √

Quicktime Movie mov - theora - mp2 √ √

Quicktime Movie mov - theora - mp3 √ √ Audio-only

Quicktime Movie mov - theora - vorbis √ √

Quicktime Movie mov - theora - wma1 √ √

Quicktime Movie mov - theora - wma2 √ √

MPEG-4 file mp4 - h264 - aac √ √ √

MPEG-4 file mp4 - h264 - dolby_digital √ √ √ √

MPEG-4 file mp4 - h264 - mp2 √ √ √ √

MPEG-4 file mp4 - h264 - mp3 √ √ √ √

MPEG-4 file mp4 - h264 - opus √ √ √

MPEG-4 file mp4 - h264 - vorbis √ √ √ √

MPEG-4 file mp4 - mpeg4 - aac Audio-only Audio-only √

MPEG-4 file mp4 - mpeg4 - mp2 Audio-only Audio-only Audio-only √

MPEG-4 file mp4 - mpeg4 - mp3 Audio-only Audio-only Audio-only √

MPEG-4 file mp4 - mpeg4 - opus Audio-only Audio-only √

MPEG-4 file mp4 - mpeg4 - vorbis Audio-only Audio-only √

MPEG-4 file mp4 - vp9 - aac √ √ √

MPEG-4 file mp4 - vp9 - dolby_digital Audio-only Audio-only Audio-only

MPEG-4 file mp4 - vp9 - mp2 √ √ √

MPEG-4 file mp4 - vp9 - mp3 √ √ √

MPEG-4 file mp4 - vp9 - opus √ √

MPEG-4 file mp4 - vp9 - vorbis √ √ √

Ogg Theora Opus ogg – theora - opus √ √ √

Ogg Theora Vorbis ogg – theora - vorbis √ √ √

Ogg VP8 Opus ogg – vp8- opus √ √ Audio-only

Ogg VP8 Vorbis ogg – vp8 - vorbis √ √

Audio-only
