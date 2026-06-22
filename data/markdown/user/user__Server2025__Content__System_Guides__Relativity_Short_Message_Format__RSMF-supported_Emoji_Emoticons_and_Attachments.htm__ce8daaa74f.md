---
title: "RSMF-supported Emoji, Emoticons, and Attachments"
url: https://help.relativity.com/Server2025/Content/System_Guides/Relativity_Short_Message_Format/RSMF-supported_Emoji_Emoticons_and_Attachments.htm
collection: user
fetched_at: 2026-06-22T06:16:24+00:00
sha256: 1197ea911ee4e3600b765dd3ec333c5b48b06e659edc9dd159ad25490e691f90
---

RSMF-supported Emoji, Emoticons, and Attachments Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

## RSMF-supported Emoji, Emoticons, and Attachments

Relativity's short message format files are compatible with a wide range of Emoji, emoticons, and attachments. Any emoji or emoticons without visual support will display as a text string instead.

This page contains the following sections:

- Supported Emoji

- Supported Emoticons

- Supported Attachments

- Supported Avatars

## Supported emoji

An emoji is a small image used alongside or instead of text in short messages. Emojis display in RSMF files as text strings surrounded by colons. For example, an emoji, :smile:, is included in the following section of a message body:

```text

	{
	"id": "1040814",=
	"type": "message",
	"conversation": "conv_default",
	"body": "Here is an emoji short name :smile:",
	"participant": "keith",
	"timestamp": "2018-09-11T09:53:01Z"
	},
```

Relativity supports displaying emoji, but not emoticons, within reactions. Emoji are also displayed within the message bodies. Emoji compatibility is dependent on your internet browser.

When emojis are rendered in HTML5, Relativity uses the native browser to render. When the emojis are imaged, the Google set is used. To learn more about the Google set, visit Emojipedia .

If an emoji is not supported, the text string for the emoji will be displayed instead. For example, if you create a custom emoji, like :test_emoji:, the text string will be displayed in the Short Message Viewer.

Only the following emoji are supported within reactions (this is not browser dependent):

Short Name Name

:+1: THUMBS UP SIGN

:-1: THUMBS DOWN SIGN

:100: HUNDRED POINTS SYMBOL

:1234: INPUT SYMBOL FOR NUMBERS

:8ball: BILLIARDS

:ab: NEGATIVE SQUARED AB

:abc: INPUT SYMBOL FOR LATIN LETTERS

:abcd: INPUT SYMBOL FOR LATIN SMALL LETTERS

:accept: CIRCLED IDEOGRAPH ACCEPT

:adult: ADULT

:aerial_tramway: AERIAL TRAMWAY

:airplane_arriving: AIRPLANE ARRIVING

:airplane_departure: AIRPLANE DEPARTURE

:alarm_clock: ALARM CLOCK

:alien: EXTRATERRESTRIAL ALIEN

:ambulance: AMBULANCE

:amphora: AMPHORA

:anchor: ANCHOR

:angel: BABY ANGEL

:anger: ANGER SYMBOL

:angry: ANGRY FACE

:anguished: ANGUISHED FACE

:ant: ANT

:apple: RED APPLE

:aquarius: AQUARIUS

:aries: ARIES

:arrow_double_down: BLACK DOWN-POINTING DOUBLE TRIANGLE

:arrow_double_up: BLACK UP-POINTING DOUBLE TRIANGLE

:arrow_down_small: DOWN-POINTING SMALL RED TRIANGLE

:arrow_up_small: UP-POINTING SMALL RED TRIANGLE

:arrows_clockwise: CLOCKWISE DOWNWARDS AND UPWARDS OPEN CIRCLE ARROWS

:arrows_counterclockwise: ANTICLOCKWISE DOWNWARDS AND UPWARDS OPEN CIRCLE ARROWS

:art: ARTIST PALETTE

:articulated_lorry: ARTICULATED LORRY

:astonished: ASTONISHED FACE

:athletic_shoe: ATHLETIC SHOE

:atm: AUTOMATED TELLER MACHINE

:avocado: AVOCADO

:baby: BABY

:baby_bottle: BABY BOTTLE

:baby_chick: BABY CHICK

:baby_symbol: BABY SYMBOL

:back: BACK WITH LEFTWARDS ARROW ABOVE

:bacon: BACON

:badminton_racquet_and_shuttlecock: BADMINTON RACQUET AND SHUTTLECOCK

:baggage_claim: BAGGAGE CLAIM

:baguette_bread: BAGUETTE BREAD

:balloon: BALLOON

:bamboo: PINE DECORATION

:banana: BANANA

:bank: BANK

:bar_chart: BAR CHART

:barber: BARBER POLE

:baseball: BASEBALL

:basketball: BASKETBALL AND HOOP

:bat: BAT

:bath: BATH

:bathtub: BATHTUB

:battery: BATTERY

:bear: BEAR FACE

:bearded_person: BEARDED PERSON

:bee: HONEYBEE

:beer: BEER MUG

:beers: CLINKING BEER MUGS

:beetle: LADY BEETLE

:beginner: JAPANESE SYMBOL FOR BEGINNER

:bell: BELL

:bento: BENTO BOX

:bicyclist: BICYCLIST

:bike: BICYCLE

:bikini: BIKINI

:billed_cap: BILLED CAP

:bird: BIRD

:birthday: BIRTHDAY CAKE

:black_circle: MEDIUM BLACK CIRCLE

:black_heart: BLACK HEART

:black_joker: PLAYING CARD BLACK JOKER

:black_large_square: BLACK LARGE SQUARE

:black_medium_small_square: BLACK MEDIUM SMALL SQUARE

:black_square_button: BLACK SQUARE BUTTON

:blossom: BLOSSOM

:blowfish: BLOWFISH

:blue_book: BLUE BOOK

:blue_car: RECREATIONAL VEHICLE

:blue_heart: BLUE HEART

:blush: SMILING FACE WITH SMILING EYES

:boar: BOAR

:boat: SAILBOAT

:bomb: BOMB

:book: OPEN BOOK

:bookmark: BOOKMARK

:bookmark_tabs: BOOKMARK TABS

:books: BOOKS

:boom: COLLISION SYMBOL

:boot: WOMANS BOOTS

:bouquet: BOUQUET

:bow: PERSON BOWING DEEPLY

:bow_and_arrow: BOW AND ARROW

:bowl_with_spoon: BOWL WITH SPOON

:bowling: BOWLING

:boxing_glove: BOXING GLOVE

:boy: BOY

:brain: BRAIN

:bread: BREAD

:breast-feeding: BREAST-FEEDING

:bride_with_veil: BRIDE WITH VEIL

:bridge_at_night: BRIDGE AT NIGHT

:briefcase: BRIEFCASE

:broccoli: BROCCOLI

:broken_heart: BROKEN HEART

:bug: BUG

:bulb: ELECTRIC LIGHT BULB

:bullettrain_front: HIGH-SPEED TRAIN WITH BULLET NOSE

:bullettrain_side: HIGH-SPEED TRAIN

:burrito: BURRITO

:bus: BUS

:busstop: BUS STOP

:bust_in_silhouette: BUST IN SILHOUETTE

:busts_in_silhouette: BUSTS IN SILHOUETTE

:butterfly: BUTTERFLY

:cactus: CACTUS

:cake: SHORTCAKE

:calendar: TEAR-OFF CALENDAR

:call_me_hand: CALL ME HAND

:calling: MOBILE PHONE WITH RIGHTWARDS ARROW AT LEFT

:camel: BACTRIAN CAMEL

:camera: CAMERA

:camera_with_flash: CAMERA WITH FLASH

:cancer: CANCER

:candy: CANDY

:canned_food: CANNED FOOD

:canoe: CANOE

:capital_abcd: INPUT SYMBOL FOR LATIN CAPITAL LETTERS

:capricorn: CAPRICORN

:car: AUTOMOBILE

:card_index: CARD INDEX

:carousel_horse: CAROUSEL HORSE

:carrot: CARROT

:cat2: CAT

:cat: CAT FACE

:cd: OPTICAL DISC

:champagne: BOTTLE WITH POPPING CORK

:chart: CHART WITH UPWARDS TREND AND YEN SIGN

:chart_with_downwards_trend: CHART WITH DOWNWARDS TREND

:chart_with_upwards_trend: CHART WITH UPWARDS TREND

:checkered_flag: CHEQUERED FLAG

:cheese_wedge: CHEESE WEDGE

:cherries: CHERRIES

:cherry_blossom: CHERRY BLOSSOM

:chestnut: CHESTNUT

:chicken: CHICKEN

:child: CHILD

:children_crossing: CHILDREN CROSSING

:chocolate_bar: CHOCOLATE BAR

:chopsticks: CHOPSTICKS

:christmas_tree: CHRISTMAS TREE

:church: CHURCH

:cinema: CINEMA

:circus_tent: CIRCUS TENT

:city_sunrise: SUNSET OVER BUILDINGS

:city_sunset: CITYSCAPE AT DUSK

:cl: SQUARED CL

:clap: CLAPPING HANDS SIGN

:clapper: CLAPPER BOARD

:clinking_glasses: CLINKING GLASSES

:clipboard: CLIPBOARD

:clock1030: CLOCK FACE TEN-THIRTY

:clock10: CLOCK FACE TEN OCLOCK

:clock1130: CLOCK FACE ELEVEN-THIRTY

:clock11: CLOCK FACE ELEVEN OCLOCK

:clock1230: CLOCK FACE TWELVE-THIRTY

:clock12: CLOCK FACE TWELVE OCLOCK

:clock130: CLOCK FACE ONE-THIRTY

:clock1: CLOCK FACE ONE OCLOCK

:clock230: CLOCK FACE TWO-THIRTY

:clock2: CLOCK FACE TWO OCLOCK

:clock330: CLOCK FACE THREE-THIRTY

:clock3: CLOCK FACE THREE OCLOCK

:clock430: CLOCK FACE FOUR-THIRTY

:clock4: CLOCK FACE FOUR OCLOCK

:clock530: CLOCK FACE FIVE-THIRTY

:clock5: CLOCK FACE FIVE OCLOCK

:clock630: CLOCK FACE SIX-THIRTY

:clock6: CLOCK FACE SIX OCLOCK

:clock730: CLOCK FACE SEVEN-THIRTY

:clock7: CLOCK FACE SEVEN OCLOCK

:clock830: CLOCK FACE EIGHT-THIRTY

:clock8: CLOCK FACE EIGHT OCLOCK

:clock930: CLOCK FACE NINE-THIRTY

:clock9: CLOCK FACE NINE OCLOCK

:closed_book: CLOSED BOOK

:closed_lock_with_key: CLOSED LOCK WITH KEY

:closed_umbrella: CLOSED UMBRELLA

:clown_face: CLOWN FACE

:coat: COAT

:cocktail: COCKTAIL GLASS

:coconut: COCONUT

:coffee: HOT BEVERAGE

:cold_sweat: FACE WITH OPEN MOUTH AND COLD SWEAT

:collision: COLLISION SYMBOL

:computer: PERSONAL COMPUTER

:confetti_ball: CONFETTI BALL

:confounded: CONFOUNDED FACE

:confused: CONFUSED FACE

:construction: CONSTRUCTION SIGN

:construction_worker: CONSTRUCTION WORKER

:convenience_store: CONVENIENCE STORE

:cookie: COOKIE

:cooking: COOKING

:cool: SQUARED COOL

:cop: POLICE OFFICER

:corn: EAR OF MAIZE

:couple: MAN AND WOMAN HOLDING HANDS

:couple_with_heart: COUPLE WITH HEART

:couplekiss: KISS

:cow2: COW

:cow: COW FACE

:crab: CRAB

:credit_card: CREDIT CARD

:crescent_moon: CRESCENT MOON

:cricket: CRICKET

:cricket_bat_and_ball: CRICKET BAT AND BALL

:crocodile: CROCODILE

:croissant: CROISSANT

:crossed_fingers: HAND WITH INDEX AND MIDDLE FINGERS CROSSED

:crossed_flags: CROSSED FLAGS

:crown: CROWN

:cry: CRYING FACE

:crying_cat_face: CRYING CAT FACE

:crystal_ball: CRYSTAL BALL

:cucumber: CUCUMBER

:cup_with_straw: CUP WITH STRAW

:cupid: HEART WITH ARROW

:curling_stone: CURLING STONE

:curly_loop: CURLY LOOP

:currency_exchange: CURRENCY EXCHANGE

:curry: CURRY AND RICE

:custard: CUSTARD

:customs: CUSTOMS

:cut_of_meat: CUT OF MEAT

:cyclone: CYCLONE

:dancer: DANCER

:dancers: WOMAN WITH BUNNY EARS

:dango: DANGO

:dart: DIRECT HIT

:dash: DASH SYMBOL

:date: CALENDAR

:deciduous_tree: DECIDUOUS TREE

:deer: DEER

:department_store: DEPARTMENT STORE

:diamond_shape_with_a_dot_inside: DIAMOND SHAPE WITH A DOT INSIDE

:disappointed: DISAPPOINTED FACE

:disappointed_relieved: DISAPPOINTED BUT RELIEVED FACE

:dizzy: DIZZY SYMBOL

:dizzy_face: DIZZY FACE

:do_not_litter: DO NOT LITTER SYMBOL

:dog2: DOG

:dog: DOG FACE

:dollar: BANKNOTE WITH DOLLAR SIGN

:dolls: JAPANESE DOLLS

:dolphin: DOLPHIN

:door: DOOR

:doughnut: DOUGHNUT

:dragon: DRAGON

:dragon_face: DRAGON FACE

:dress: DRESS

:dromedary_camel: DROMEDARY CAMEL

:drooling_face: DROOLING FACE

:droplet: DROPLET

:drum_with_drumsticks: DRUM WITH DRUMSTICKS

:duck: DUCK

:dumpling: DUMPLING

:dvd: DVD

:e-mail: E-MAIL SYMBOL

:eagle: EAGLE

:ear: EAR

:ear_of_rice: EAR OF RICE

:earth_africa: EARTH GLOBE EUROPE-AFRICA

:earth_americas: EARTH GLOBE AMERICAS

:earth_asia: EARTH GLOBE ASIA-AUSTRALIA

:egg: EGG

:eggplant: AUBERGINE

:electric_plug: ELECTRIC PLUG

:elephant: ELEPHANT

:elf: ELF

:end: END WITH LEFTWARDS ARROW ABOVE

:envelope_with_arrow: ENVELOPE WITH DOWNWARDS ARROW ABOVE

:euro: BANKNOTE WITH EURO SIGN

:european_castle: EUROPEAN CASTLE

:european_post_office: EUROPEAN POST OFFICE

:evergreen_tree: EVERGREEN TREE

:exclamation: HEAVY EXCLAMATION MARK SYMBOL

:exploding_head: SHOCKED FACE WITH EXPLODING HEAD

:expressionless: EXPRESSIONLESS FACE

:eyeglasses: EYEGLASSES

:eyes: EYES

:face_palm: FACE PALM

:face_vomiting: FACE WITH OPEN MOUTH VOMITING

:face_with_cowboy_hat: FACE WITH COWBOY HAT

:face_with_finger_covering_closed_lips: FACE WITH FINGER COVERING CLOSED LIPS

:face_with_hand_over_mouth: SMILING FACE WITH SMILING EYES AND HAND COVERING MOUTH

:face_with_head_bandage: FACE WITH HEAD-BANDAGE

:face_with_monocle: FACE WITH MONOCLE

:face_with_one_eyebrow_raised: FACE WITH ONE EYEBROW RAISED

:face_with_open_mouth_vomiting: FACE WITH OPEN MOUTH VOMITING

:face_with_raised_eyebrow: ACE WITH ONE EYEBROW RAISED

:face_with_rolling_eyes: FACE WITH ROLLING EYES

:face_with_symbols_on_mouth: SERIOUS FACE WITH SYMBOLS COVERING MOUTH

:face_with_thermometer: FACE WITH THERMOMETER

:facepunch: FISTED HAND SIGN

:factory: FACTORY

:fairy: FAIRY

:fallen_leaf: FALLEN LEAF

:family: FAMILY

:fast_forward: BLACK RIGHT-POINTING DOUBLE TRIANGLE

:fax: FAX MACHINE

:fearful: FEARFUL FACE

:feet: PAW PRINTS

:fencer: FENCER

:ferris_wheel: FERRIS WHEEL

:field_hockey_stick_and_ball: FIELD HOCKEY STICK AND BALL

:file_folder: FILE FOLDER

:fire: FIRE

:fire_engine: FIRE ENGINE

:fireworks: FIREWORKS

:first_place_medal: FIRST PLACE MEDAL

:first_quarter_moon: FIRST QUARTER MOON SYMBOL

:first_quarter_moon_with_face: FIRST QUARTER MOON WITH FACE

:fish: FISH

:fish_cake: FISH CAKE WITH SWIRL DESIGN

:fishing_pole_and_fish: FISHING POLE AND FISH

:fist: RAISED FIST

:flags: CARP STREAMER

:flashlight: ELECTRIC TORCH

:flipper: DOLPHIN

:floppy_disk: FLOPPY DISK

:flower_playing_cards: FLOWER PLAYING CARDS

:flushed: FLUSHED FACE

:flying_saucer: FLYING SAUCER

:foggy: FOGGY

:football: AMERICAN FOOTBALL

:footprints: FOOTPRINTS

:fork_and_knife: FORK AND KNIFE

:fortune_cookie: FORTUNE COOKIE

:fountain: FOUNTAIN

:four_leaf_clover: FOUR LEAF CLOVER

:fox_face: FOX FACE

:free: SQUARED FREE

:fried_egg: COOKING

:fried_shrimp: FRIED SHRIMP

:fries: FRENCH FRIES

:frog: FROG FACE

:frowning: FROWNING FACE WITH OPEN MOUTH

:fuelpump: FUEL PUMP

:full_moon: FULL MOON SYMBOL

:full_moon_with_face: FULL MOON WITH FACE

:game_die: GAME DIE

:gem: GEM STONE

:gemini: GEMINI

:genie: GENIE

:ghost: GHOST

:gift: WRAPPED PRESENT

:gift_heart: HEART WITH RIBBON

:giraffe_face: GIRAFFE FACE

:girl: GIRL

:glass_of_milk: GLASS OF MILK

:globe_with_meridians: GLOBE WITH MERIDIANS

:gloves: GLOVES

:goal_net: GOAL NET

:goat: GOAT

:golf: FLAG IN HOLE

:gorilla: GORILLA

:grapes: GRAPES

:green_apple: GREEN APPLE

:green_book: GREEN BOOK

:green_heart: GREEN HEART

:green_salad: GREEN SALAD

:grey_exclamation: WHITE EXCLAMATION MARK ORNAMENT

:grey_question: WHITE QUESTION MARK ORNAMENT

:grimacing: GRIMACING FACE

:grin: GRINNING FACE WITH SMILING EYES

:grinning: GRINNING FACE

:grinning_face_with_one_large_and_one_small_eye: GRINNING FACE WITH ONE LARGE AND ONE SMALL EYE

:grinning_face_with_star_eyes: GRINNING FACE WITH STAR EYES

:guardsman: GUARDSMAN

:guitar: GUITAR

:gun: PISTOL

:haircut: HAIRCUT

:hamburger: HAMBURGER

:hammer: HAMMER

:hamster: HAMSTER FACE

:hand: RAISED HAND

:hand_with_index_and_middle_fingers_crossed: HAND WITH INDEX AND MIDDLE FINGERS CROSSED

:handbag: HANDBAG

:handball: HANDBALL

:handshake: HANDSHAKE

:hankey: PILE OF POO

:hatched_chick: FRONT-FACING BABY CHICK

:hatching_chick: HATCHING CHICK

:headphones: HEADPHONE

:hear_no_evil: HEAR-NO-EVIL MONKEY

:heart_decoration: HEART DECORATION

:heart_eyes: SMILING FACE WITH HEART-SHAPED EYES

:heart_eyes_cat: SMILING CAT FACE WITH HEART-SHAPED EYE

:heartbeat: BEATING HEART

:heartpulse: GROWING HEART

:heavy_division_sign: HEAVY DIVISION SIGN

:heavy_dollar_sign: HEAVY DOLLAR SIGN

:heavy_exclamation_mark: HEAVY EXCLAMATION MARK SYMBOL

:heavy_minus_sign: HEAVY MINUS SIGN

:heavy_plus_sign: HEAVY PLUS SIGN

:hedgehog: HEDGEHOG

:helicopter: HELICOPTER

:herb: HERB

:hibiscus: HIBISCUS

:high_brightness: HIGH BRIGHTNESS SYMBOL

:high_heel: HIGH-HEELED SHOE

:hocho: HOCHO

:honey_pot: HONEY POT

:honeybee: HONEYBEE

:horse: HORSE FACE

:horse_racing: HORSE RACING

:hospital: HOSPITAL

:hotdog: HOT DOG

:hotel: HOTEL

:hourglass: HOURGLASS

:hourglass_flowing_sand: HOURGLASS WITH FLOWING SAND

:house: HOUSE BUILDING

:house_with_garden: HOUSE WITH GARDEN

:hugging_face: HUGGING FACE

:hushed: HUSHED FACE

:i_love_you_hand_sign: I LOVE YOU HAND SIGN

:ice_cream: ICE CREAM

:ice_hockey_stick_and_puck: ICE HOCKEY STICK AND PUCK

:icecream: SOFT ICE CREAM

:id: SQUARED ID

:ideograph_advantage: CIRCLED IDEOGRAPH ADVANTAGE

:imp: IMP

:inbox_tray: INBOX TRAY

:incoming_envelope: INCOMING ENVELOPE

:information_desk_person: INFORMATION DESK PERSON

:innocent: SMILING FACE WITH HALO

:iphone: MOBILE PHONE

:izakaya_lantern: IZAKAYA LANTERN

:jack_o_lantern: JACK-O-LANTERN

:japan: SILHOUETTE OF JAPAN

:japanese_castle: JAPANESE CASTLE

:japanese_goblin: JAPANESE GOBLIN

:japanese_ogre: JAPANESE OGRE

:jeans: JEANS

:joy: FACE WITH TEARS OF JOY

:joy_cat: CAT FACE WITH TEARS OF JOY

:juggling: JUGGLING

:kaaba: KAABA

:key: KEY

:keycap_ten: KEYCAP TEN

:kimono: KIMONO

:kiss: KISS MARK

:kissing: KISSING FACE

:kissing_cat: KISSING CAT FACE WITH CLOSED EYES

:kissing_closed_eyes: KISSING FACE WITH CLOSED EYES

:kissing_heart: FACE THROWING A KISS

:kissing_smiling_eyes: KISSING FACE WITH SMILING EYES

:kiwifruit: KIWIFRUIT

:knife: KNIFE

:koala: KOALA

:koko: SQUARED KATAKANA KOKO

:lantern: IZAKAYA LANTERN

:large_blue_circle: LARGE BLUE CIRCLE

:large_blue_diamond: LARGE BLUE DIAMOND

:large_orange_diamond: LARGE ORANGE DIAMOND

:last_quarter_moon: LAST QUARTER MOON SYMBOL

:last_quarter_moon_with_face: LAST QUARTER MOON WITH FACE

:laughing: SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES

:leaves: LEAF FLUTTERING IN WIND

:ledger: LEDGER

:left-facing_fist: LEFT-FACING FIST

:left_luggage: LEFT LUGGAGE

:lemon: LEMON

:leo: LEO

:leopard: LEOPARD

:libra: LIBRA

:light_rail: LIGHT RAIL

:link: LINK SYMBOL

:lion_face: LION FACE

:lips: MOUTH

:lipstick: LIPSTICK

:lizard: LIZARD

:lock: LOCK

:lock_with_ink_pen: LOCK WITH INK PEN

:lollipop: LOLLIPOP

:loop: DOUBLE CURLY LOOP

:loud_sound: SPEAKER WITH THREE SOUND WAVES

:loudspeaker: PUBLIC ADDRESS LOUDSPEAKER

:love_hotel: LOVE HOTEL

:love_letter: LOVE LETTER

:low_brightness: LOW BRIGHTNESS SYMBOL

:lying_face: LYING FACE

:mag: LEFT-POINTING MAGNIFYING GLASS

:mag_right: RIGHT-POINTING MAGNIFYING GLASS

:mage: MAGE

:mahjong: MAHJONG TILE RED DRAGON

:mailbox: CLOSED MAILBOX WITH RAISED FLAG

:mailbox_closed: CLOSED MAILBOX WITH LOWERED FLAG

:mailbox_with_mail: OPEN MAILBOX WITH RAISED FLAG

:mailbox_with_no_mail: OPEN MAILBOX WITH LOWERED FLAG

:man-woman-boy: FAMILY

:man: MAN

:man_and_woman_holding_hands: MAN AND WOMAN HOLDING HANDS

:man_dancing: MAN DANCING

:man_in_tuxedo: MAN IN TUXEDO

:man_with_gua_pi_mao: MAN WITH GUA PI MAO

:man_with_turban: MAN WITH TURBAN

:mans_shoe: MANS SHOE

:maple_leaf: MAPLE LEAF

:martial_arts_uniform: MARTIAL ARTS UNIFORM

:mask: FACE WITH MEDICAL MASK

:massage: FACE MASSAGE

:meat_on_bone: MEAT ON BONE

:mega: CHEERING MEGAPHONE

:melon: MELON

:memo: MEMO

:menorah_with_nine_branches: MENORAH WITH NINE BRANCHES

:mens: MENS SYMBOL

:merperson: MERPERSON

:metro: METRO

:microphone: MICROPHONE

:microscope: MICROSCOPE

:middle_finger: REVERSED HAND WITH MIDDLE FINGER EXTENDED

:milky_way: MILKY WAY

:minibus: MINIBUS

:minidisc: MINIDISC

:mobile_phone_off: MOBILE PHONE OFF

:money_mouth_face: MONEY-MOUTH FACE

:money_with_wings: MONEY WITH WINGS

:moneybag: MONEY BAG

:monkey: MONKEY

:monkey_face: MONKEY FACE

:monorail: MONORAIL

:moon: WAXING GIBBOUS MOON SYMBOL

:mortar_board: GRADUATION CAP

:mosque: MOSQUE

:mother_christmas: MOTHER CHRISTMAS

:motor_scooter: MOTOR SCOOTER

:mount_fuji: MOUNT FUJI

:mountain_bicyclist: MOUNTAIN BICYCLIST

:mountain_cableway: MOUNTAIN CABLEWAY

:mountain_railway: MOUNTAIN RAILWAY

:mouse2: MOUSE

:mouse: MOUSE FACE

:movie_camera: MOVIE CAMERA

:moyai: MOYAI

:mrs_claus: MOTHER CHRISTMAS

:muscle: FLEXED BICEPS

:mushroom: MUSHROOM

:musical_keyboard: MUSICAL KEYBOARD

:musical_note: MUSICAL NOTE

:musical_score: MUSICAL SCORE

:mute: SPEAKER WITH CANCELLATION STROKE

:nail_care: NAIL POLISH

:name_badge: NAME BADGE

:nauseated_face: NAUSEATED FACE

:necktie: NECKTIE

:negative_squared_cross_mark: NEGATIVE SQUARED CROSS MARK

:nerd_face: NERD FACE

:neutral_face: NEUTRAL FACE

:new: SQUARED NEW

:new_moon: NEW MOON SYMBOL

:new_moon_with_face: NEW MOON WITH FACE

:newspaper: NEWSPAPER

:ng: SQUARED NG

:night_with_stars: NIGHT WITH STARS

:no_bell: BELL WITH CANCELLATION STROKE

:no_bicycles: NO BICYCLES

:no_entry: NO ENTRY

:no_entry_sign: NO ENTRY SIGN

:no_good: FACE WITH NO GOOD GESTURE

:no_mobile_phones: NO MOBILE PHONES

:no_mouth: FACE WITHOUT MOUTH

:no_pedestrians: NO PEDESTRIANS

:no_smoking: NO SMOKING SYMBOL

:non-potable_water: NON-POTABLE WATER SYMBOL

:nose: NOSE

:notebook: NOTEBOOK

:notebook_with_decorative_cover: NOTEBOOK WITH DECORATIVE COVER

:notes: MULTIPLE MUSICAL NOTES

:nut_and_bolt: NUT AND BOLT

:o: HEAVY LARGE CIRCLE

:ocean: WATER WAVE

:octagonal_sign: OCTAGONAL SIGN

:octopus: OCTOPUS

:oden: ODEN

:office: OFFICE BUILDING

:ok: SQUARED OK

:ok_hand: OK HAND SIGN

:ok_woman: FACE WITH OK GESTURE

:older_adult: OLDER ADULT

:older_man: OLDER MAN

:older_woman: OLDER WOMAN

:on: ON WITH EXCLAMATION MARK WITH LEFT RIGHT ARROW ABOVE

:oncoming_automobile: ONCOMING AUTOMOBILE

:oncoming_bus: ONCOMING BUS

:oncoming_police_car: ONCOMING POLICE CAR

:oncoming_taxi: ONCOMING TAXI

:open_book: OPEN BOOK

:open_file_folder: OPEN FILE FOLDER

:open_hands: OPEN HANDS SIGN

:open_mouth: FACE WITH OPEN MOUTH

:ophiuchus: OPHIUCHUS

:orange_book: ORANGE BOOK

:orange_heart: ORANGE HEART

:outbox_tray: OUTBOX TRAY

:owl: OWL

:ox: OX

:package: PACKAGE

:page_facing_up: PAGE FACING UP

:page_with_curl: PAGE WITH CURL

:pager: PAGER

:palm_tree: PALM TREE

:palms_up_together: PALMS UP TOGETHER

:pancakes: PANCAKES

:panda_face: PANDA FACE

:paperclip: PAPERCLIP

:partly_sunny: SUN BEHIND CLOUD

:passport_control: PASSPORT CONTROL

:paw_prints: PAW PRINTS

:peach: PEACH

:peanuts: PEANUTS

:pear: PEAR

:pencil: MEMO

:penguin: PENGUIN

:pensive: PENSIVE FACE

:performing_arts: PERFORMING ARTS

:persevere: PERSEVERING FACE

:person_climbing: PERSON CLIMBING

:person_doing_cartwheel: PERSON DOING CARTWHEEL

:person_frowning: PERSON FROWNING

:person_in_lotus_position: PERSON IN LOTUS POSITION

:person_in_steamy_room: PERSON IN STEAMY ROOM

:person_with_blond_hair: PERSON WITH BLOND HAIR

:person_with_headscarf: PERSON WITH HEADSCARF

:person_with_pouting_face: PERSON WITH POUTING FACE

:pie: PIE

:pig2: PIG

:pig: PIG FACE

:pig_nose: PIG NOSE

:pill: PILL

:pineapple: PINEAPPLE

:pisces: PISCES

:pizza: SLICE OF PIZZA

:place_of_worship: PLACE OF WORSHIP

:point_down: WHITE DOWN POINTING BACKHAND INDEX

:point_left: WHITE LEFT POINTING BACKHAND INDEX

:point_right: WHITE RIGHT POINTING BACKHAND INDEX

:point_up_2: WHITE UP POINTING BACKHAND INDEX

:police_car: POLICE CAR

:poodle: POODLE

:poop: PILE OF POO

:popcorn: POPCORN

:post_office: JAPANESE POST OFFICE

:postal_horn: POSTAL HORN

:postbox: POSTBOX

:potable_water: POTABLE WATER SYMBOL

:potato: POTATO

:pouch: POUCH

:poultry_leg: POULTRY LEG

:pound: BANKNOTE WITH POUND SIGN

:pouting_cat: POUTING CAT FACE

:pray: PERSON WITH FOLDED HANDS

:prayer_beads: PRAYER BEADS

:pregnant_woman: PREGNANT WOMAN

:pretzel: PRETZEL

:prince: PRINCE

:princess: PRINCESS

:punch: FISTED HAND SIGN

:purple_heart: PURPLE HEART

:purse: PURSE

:pushpin: PUSHPIN

:put_litter_in_its_place: PUT LITTER IN ITS PLACE SYMBOL

:question: BLACK QUESTION MARK ORNAMENT

:rabbit2: RABBIT

:rabbit: RABBIT FACE

:racehorse: HORSE

:radio: RADIO

:radio_button: RADIO BUTTON

:rage: POUTING FACE

:railway_car: RAILWAY CAR

:rainbow: RAINBOW

:raised_back_of_hand: RAISED BACK OF HAND

:raised_hand: RAISED HAND

:raised_hands: PERSON RAISING BOTH HANDS IN CELEBRATION

:raising_hand: HAPPY PERSON RAISING ONE HAND

:ram: RAM

:ramen: STEAMING BOWL

:rat: RAT

:red_car: AUTOMOBILE

:red_circle: LARGE RED CIRCLE

:relieved: RELIEVED FACE

:repeat: CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS

:repeat_one: CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS WITH CIRCLED ONE OVERLAY

:restroom: RESTROOM

:reversed_hand_with_middle_finger_extended: REVERSED HAND WITH MIDDLE FINGER EXTENDED

:revolving_hearts: REVOLVING HEARTS

:rewind: BLACK LEFT-POINTING DOUBLE TRIANGLE

:rhinoceros: RHINOCEROS

:ribbon: RIBBON

:rice: COOKED RICE

:rice_ball: RICE BALL

:rice_cracker: RICE CRACKER

:rice_scene: MOON VIEWING CEREMONY

:right-facing_fist: RIGHT-FACING FIST

:ring: RING

:robot_face: ROBOT FACE

:rocket: ROCKET

:roller_coaster: ROLLER COASTER

:rolling_on_the_floor_laughing: ROLLING ON THE FLOOR LAUGHING

:rooster: ROOSTER

:rose: ROSE

:rotating_light: POLICE CARS REVOLVING LIGHT

:round_pushpin: ROUND PUSHPIN

:rowboat: ROWBOAT

:rugby_football: RUGBY FOOTBALL

:runner: RUNNER

:running: RUNNER

:running_shirt_with_sash: RUNNING SHIRT WITH SASH

:sagittarius: SAGITTARIUS

:sailboat: SAILBOAT

:sake: SAKE BOTTLE AND CUP

:sandal: WOMANS SANDAL

:sandwich: SANDWICH

:santa: FATHER CHRISTMAS

:satellite_antenna: SATELLITE ANTENNA

:satisfied: SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES

:sauropod: SAUROPOD

:saxophone: SAXOPHONE

:scarf: SCARF

:school: SCHOOL

:school_satchel: SCHOOL SATCHEL

:scooter: SCOOTER

:scorpion: SCORPION

:scorpius: SCORPIUS

:scream: FACE SCREAMING IN FEAR

:scream_cat: WEARY CAT FACE

:scroll: SCROLL

:seat: SEAT

:second_place_medal: SECOND PLACE MEDAL

:see_no_evil: SEE-NO-EVIL MONKEY

:seedling: SEEDLING

:selfie: SELFIE

:serious_face_with_symbols_covering_mouth: SERIOUS FACE WITH SYMBOLS COVERING MOUTH

:shallow_pan_of_food: SHALLOW PAN OF FOOD

:shark: SHARK

:shaved_ice: SHAVED ICE

:sheep: SHEEP

:shell: SPIRAL SHELL

:ship: SHIP

:shirt: T-SHIRT

:shit: PILE OF POO

:shocked_face_with_exploding_head: SHOCKED FACE WITH EXPLODING HEAD

:shoe: MANS SHOE

:shopping_trolley: SHOPPING TROLLEY

:shower: SHOWER

:shrimp: SHRIMP

:shrug: SHRUG

:shushing_face: FACE WITH FINGER COVERING CLOSED LIPS

:sign_of_the_horns: SIGN OF THE HORNS

:signal_strength: ANTENNA WITH BARS

:six_pointed_star: SIX POINTED STAR WITH MIDDLE DOT

:ski: SKI AND SKI BOOT

:skin-tone-2: EMOJI MODIFIER FITZPATRICK TYPE-1-2

:skin-tone-3: MOJI MODIFIER FITZPATRICK TYPE-3

:skin-tone-4: EMOJI MODIFIER FITZPATRICK TYPE-4

:skin-tone-5: EMOJI MODIFIER FITZPATRICK TYPE-5

:skin-tone-6: EMOJI MODIFIER FITZPATRICK TYPE-6

:skull: SKULL

:sled: SLED

:sleeping: SLEEPING FACE

:sleeping_accommodation: SLEEPING ACCOMMODATION

:sleepy: SLEEPY FACE

:slightly_frowning_face: SLIGHTLY FROWNING FACE

:slightly_smiling_face: SLIGHTLY SMILING FACE

:slot_machine: SLOT MACHINE

:small_blue_diamond: SMALL BLUE DIAMOND

:small_orange_diamond: SMALL ORANGE DIAMOND

:small_red_triangle: UP-POINTING RED TRIANGLE

:small_red_triangle_down: DOWN-POINTING RED TRIANGLE

:smile: SMILING FACE WITH OPEN MOUTH AND SMILING EYES

:smile_cat: GRINNING CAT FACE WITH SMILING EYES

:smiley: SMILING FACE WITH OPEN MOUTH

:smiley_cat: SMILING CAT FACE WITH OPEN MOUTH

:smiling_face_with_smiling_eyes_and_hand_covering_mouth: SMILING FACE WITH SMILING EYES AND HAND COVERING MOUTH

:smiling_imp: SMILING FACE WITH HORNS

:smirk: SMIRKING FACE

:smirk_cat: CAT FACE WITH WRY SMILE

:smoking: SMOKING SYMBOL

:snail: SNAIL

:snake: SNAKE

:sneezing_face: SNEEZING FACE

:snowboarder: SNOWBOARDER

:snowman_without_snow: SNOWMAN WITHOUT SNOW

:sob: LOUDLY CRYING FACE

:soccer: SOCCER BALL

:socks: SOCKS

:soon: SOON WITH RIGHTWARDS ARROW ABOVE

:sos: SQUARED SOS

:sound: SPEAKER WITH ONE SOUND WAVE

:space_invader: ALIEN MONSTER

:spaghetti: SPAGHETTI

:sparkler: FIREWORK SPARKLER

:sparkles: SPARKLES

:sparkling_heart: SPARKLING HEART

:speak_no_evil: SPEAK-NO-EVIL MONKEY

:speaker: SPEAKER

:speech_balloon: SPEECH BALLOON

:speedboat: SPEEDBOAT

:spock-hand: RAISED HAND WITH PART BETWEEN MIDDLE AND RING FINGERS

:spoon: SPOON

:sports_medal: SPORTS MEDAL

:squid: SQUID

:star-struck: GRINNING FACE WITH STAR EYES

:star2: GLOWING STAR

:star: WHITE MEDIUM STAR

:stars: SHOOTING STAR

:station: STATION

:statue_of_liberty: STATUE OF LIBERTY

:steam_locomotive: STEAM LOCOMOTIVE

:stew: POT OF FOOD

:straight_ruler: STRAIGHT RULER

:strawberry: STRAWBERRY

:stuck_out_tongue: FACE WITH STUCK-OUT TONGUE

:stuck_out_tongue_closed_eyes: FACE WITH STUCK-OUT TONGUE AND TIGHTLY-CLOSED EYES

:stuck_out_tongue_winking_eye: FACE WITH STUCK-OUT TONGUE AND WINKING EYE

:stuffed_flatbread: STUFFED FLATBREAD

:sun_with_face: SUN WITH FACE

:sunflower: SUNFLOWER

:sunglasses: SMILING FACE WITH SUNGLASSES

:sunrise: SUNRISE

:sunrise_over_mountains: SUNRISE OVER MOUNTAINS

:surfer: SURFER

:sushi: SUSHI

:suspension_railway: SUSPENSION RAILWAY

:sweat: FACE WITH COLD SWEAT

:sweat_drops: SPLASHING SWEAT SYMBOL

:sweat_smile: SMILING FACE WITH OPEN MOUTH AND COLD SWEAT

:sweet_potato: ROASTED SWEET POTATO

:swimmer: SWIMMER

:symbols: INPUT SYMBOL FOR SYMBOLS

:synagogue: SYNAGOGUE

:syringe: SYRINGE

:t-rex: T-REX

:table_tennis_paddle_and_ball: TABLE TENNIS PADDLE AND BALL

:taco: TACO

:tada: PARTY POPPER

:takeout_box: TAKEOUT BOX

:tanabata_tree: TANABATA TREE

:tangerine: TANGERINE

:taurus: TAURUS

:taxi: TAXI

:tea: TEACUP WITHOUT HANDLE

:telephone_receiver: TELEPHONE RECEIVER

:telescope: TELESCOPE

:tennis: TENNIS RACQUET AND BALL

:tent: TENT

:the_horns: SIGN OF THE HORNS

:thinking_face: THINKING FACE

:third_place_medal: THIRD PLACE MEDAL

:thought_balloon: THOUGHT BALLOON

:thumbsdown: THUMBS DOWN SIGN

:thumbsup: THUMBS UP SIGN

:ticket: TICKET

:tiger2: TIGER

:tiger: TIGER FACE

:tired_face: TIRED FACE

:toilet: TOILET

:tokyo_tower: TOKYO TOWER

:tomato: TOMATO

:tongue: TONGUE

:top: TOP WITH UPWARDS ARROW ABOVE

:tophat: TOP HAT

:tractor: TRACTOR

:traffic_light: HORIZONTAL TRAFFIC LIGHT

:train2: TRAIN

:train: TRAM CAR

:tram: TRAM

:triangular_flag_on_post: TRIANGULAR FLAG ON POST

:triangular_ruler: TRIANGULAR RULER

:trident: TRIDENT EMBLEM

:triumph: FACE WITH LOOK OF TRIUMPH

:trolleybus: TROLLEYBUS

:trophy: TROPHY

:tropical_drink: TROPICAL DRINK

:tropical_fish: TROPICAL FISH

:truck: DELIVERY TRUCK

:trumpet: TRUMPET

:tshirt: T-SHIRT

:tulip: TULIP

:tumbler_glass: TUMBLER GLASS

:turkey: TURKEY

:turtle: TURTLE

:tv: TELEVISION

:twisted_rightwards_arrows: TWISTED RIGHTWARDS ARROWS

:two_hearts: TWO HEARTS

:two_men_holding_hands: TWO MEN HOLDING HANDS

:two_women_holding_hands: TWO WOMEN HOLDING HANDS

:u5272: SQUARED CJK UNIFIED IDEOGRAPH-5272

:u5408: SQUARED CJK UNIFIED IDEOGRAPH-5408

:u55b6: SQUARED CJK UNIFIED IDEOGRAPH-55B6

:u6307: SQUARED CJK UNIFIED IDEOGRAPH-6307

:u6709: SQUARED CJK UNIFIED IDEOGRAPH-6709

:u6e80: SQUARED CJK UNIFIED IDEOGRAPH-6E80

:u7121: SQUARED CJK UNIFIED IDEOGRAPH-7121

:u7533: SQUARED CJK UNIFIED IDEOGRAPH-7533

:u7981: SQUARED CJK UNIFIED IDEOGRAPH-7981

:u7a7a: SQUARED CJK UNIFIED IDEOGRAPH-7A7A

:umbrella_with_rain_drops: UMBRELLA WITH RAIN DROPS

:unamused: UNAMUSED FACE

:underage: NO ONE UNDER EIGHTEEN SYMBOL

:unicorn_face: UNICORN FACE

:unlock: OPEN LOCK

:up: SQUARED UP WITH EXCLAMATION MARK

:upside_down_face: UPSIDE-DOWN FACE

:vampire: VAMPIRE

:vertical_traffic_light: VERTICAL TRAFFIC LIGHT

:vhs: VIDEOCASSETTE

:vibration_mode: VIBRATION MODE

:video_camera: VIDEO CAMERA

:video_game: VIDEO GAME

:violin: VIOLIN

:virgo: VIRGO

:volcano: VOLCANO

:volleyball: VOLLEYBALL

:vs: SQUARED VS

:walking: PEDESTRIAN

:waning_crescent_moon: WANING CRESCENT MOON SYMBOL

:waning_gibbous_moon: WANING GIBBOUS MOON SYMBOL

:watch: WATCH

:water_buffalo: WATER BUFFALO

:water_polo: WATER POLO

:watermelon: WATERMELON

:wave: WAVING HAND SIGN

:waving_black_flag: WAVING BLACK FLAG

:waxing_crescent_moon: WAXING CRESCENT MOON SYMBOL

:waxing_gibbous_moon: WAXING GIBBOUS MOON SYMBOL

:wc: WATER CLOSET

:weary: WEARY FACE

:wedding: WEDDING

:whale2: WHALE

:whale: SPOUTING WHALE

:wheelchair: WHEELCHAIR SYMBOL

:white_check_mark: WHITE HEAVY CHECK MARK

:white_circle: MEDIUM WHITE CIRCLE

:white_flower: WHITE FLOWER

:white_large_square: WHITE LARGE SQUARE

:white_medium_small_square: WHITE MEDIUM SMALL SQUARE

:white_square_button: WHITE SQUARE BUTTON

:wilted_flower: WILTED FLOWER

:wind_chime: WIND CHIME

:wine_glass: WINE GLASS

:wink: WINKING FACE

:wolf: WOLF FACE

:woman: WOMAN

:womans_clothes: WOMANS CLOTHES

:womans_hat: WOMANS HAT

:womens: WOMENS SYMBOL

:worried: WORRIED FACE

:wrench: WRENCH

:wrestlers: WRESTLERS

:x: CROSS MARK

:yellow_heart: YELLOW HEART

:yen: BANKNOTE WITH YEN SIGN

:yum: FACE SAVOURING DELICIOUS FOOD

:zany_face: GRINNING FACE WITH ONE LARGE AND ONE SMALL EYE

:zap: HIGH VOLTAGE SIGN

:zebra_face: ZEBRA FACE

:zipper_mouth_face: ZIPPER-MOUTH FACE

:zombie: ZOMBIE

:zzz: SLEEPING SYMBOL

## Supported emoticons

An emoticon is a sequence of keyboard characters used to illustrate a facial expression or to render some kind of picture or symbol. For example, the emoticon, :-), is included in the following section of a message body:

```text

	{
	"id": "1040807",

	"type": "message",

	"conversation": "conv_default",

	"body": "Here is an emoticon:  :-)",

	"participant": "karl",

	"timestamp": "2018-09-11T09:50:00Z"
	 },

```

Relativity supports emoticons within a message body. The following emoticons are supported:

Search Term Name

"<3" red heart

"</3" broken heart

":D" grinning face with big eyes

":-D" grinning face with big eyes

"=D" grinning face with big eyes

">:)" grinning squinting face

">;)" grinning squinting face

">:-)" grinning squinting face

">=)" grinning squinting face

"':)" grinning face with sweat

"':-)" grinning face with sweat

"'=)" grinning face with sweat

"':D" grinning face with sweat

"':-D" grinning face with sweat

"'=D" grinning face with sweat

":')" face with tears of joy

":'-)" face with tears of joy

"O:-)" smiling face with halo

"0:-3" smiling face with halo

"0:3" smiling face with halo

"0:-)" smiling face with halo

"0:)" smiling face with halo

"0;^)" smiling face with halo

"O:)" smiling face with halo

"O;-)" smiling face with halo

"O=)" smiling face with halo

"0;-)" smiling face with halo

"O:-3" smiling face with halo

"O:3" smiling face with halo

":)" slightly smiling face

":-)" slightly smiling face

"=]" slightly smiling face

"=)" slightly smiling face

":]" slightly smiling face

";)" winking face

";-)" winking face

"*-)" winking face

"*)" winking face

";-]" winking face

";]" winking face

";D" winking face

";^)" winking face

":*" face blowing a kiss

":-*" face blowing a kiss

"=*" face blowing a kiss

":^*" face blowing a kiss

":P" face with tongue

":-P" face with tongue

"=P" face with tongue

":-Þ" face with tongue

":Þ" face with tongue

":-b" face with tongue

":b" face with tongue

">:P" winking face with tongue

"X-P" winking face with tongue

"B-)" smiling face with sunglasses

"B)" smiling face with sunglasses

"8)" smiling face with sunglasses

"8-)" smiling face with sunglasses

"B-D" smiling face with sunglasses

"8-D" smiling face with sunglasses

">:[" disappointed face

":-(" disappointed face

":(" disappointed face

":-[" disappointed face

":[" disappointed face

"=(" disappointed face

">:\\" confused face

">:/" confused face

":-/" confused face

":-." confused face

":\\" confused face

"=/" confused face

"=\\" confused face

":L" confused face

"=L" confused face

">.<" persevering face

":'(" crying face

":'-(" crying face

";(" crying face

";-(" crying face

">:(" angry face

">:-(" angry face

":@" angry face

":$" flushed face

"=$" flushed face

"D:" fearful face

"':(" downcast face with sweat

"':-(" downcast face with sweat

"'=(" downcast face with sweat

":-X" face without mouth

":X" face without mouth

":-#" face without mouth

":#" face without mouth

"=X" face without mouth

"=#" face without mouth

"-_-" expressionless face

"-__-" expressionless face

"-___-" expressionless face

":-O" face with open mouth

":O" face with open mouth

"O_O" face with open mouth

">:O" face with open mouth

"#-)" dizzy face

"#)" dizzy face

"%-)" dizzy face

"%)" dizzy face

"X)" dizzy face

"X-)" dizzy face

"(y)" thumbs up

"*\\0/*" person gesturing OK

"\\0/" person gesturing OK

"*\\O/*" person gesturing OK

"\\O/" person gesturing OK

## Supported attachments

Relativity renders attachments based on the extension of the display value of an attachment. There are two important considerations:

- If the extension ends in .png, .jpg, ,jpeg, or .gif, the system will attempt to render it in-line.

- All other extensions are rendered as attachments with icons. Some file extensions have custom icons as defined below:

Icon Extensions

ics

ai

cdr

cgm

dgn

drw

dwg

dxf

emf

gdf

gem

hpgl

odg

pic

pif

ps

svg

wmf

bmp

cur

dcx

ico

img

indd

odi

pbm

pcd

pct

pcx

pdfi

pgm

ppm

psd

psp

sdw

tga

tif

wbmp

wpg

xbm

xpm

chtml

hdml

htm

html

mhtml

wml

xhtml

xml

xmp

doc

docx

eml

msg

pst

fft

lwp

odt

oft

rtf

txt

wpd

yim

mpg

wmv

mpp

pdf

ppt

pptx

vsd

xlc

xls

xlsb

xlsx

zip

## Supported avatars

Only PNG, JPG, and GIF image formats are supported for avatars.

On this page

- RSMF-supported Emoji, Emoticons, and Attachments

- Supported emoji

- Supported emoticons

- Supported attachments

- Supported avatars


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
