import sys, pathlib, hashlib
OUT = pathlib.Path(sys.argv[1])
CSSV = hashlib.md5((OUT/"style.css").read_bytes()).hexdigest()[:8]
JSV = hashlib.md5((OUT/"lang.js").read_bytes()).hexdigest()[:8]
UPDATED_FR = "22 octobre 2026"; UPDATED_EN = "October 22, 2026"

def F(fr, en, tag="span"):
    return f'<{tag} data-l="fr">{fr}</{tag}><{tag} data-l="en">{en}</{tag}>'

def head(t_fr, t_en, d_fr, d_en):
    return f'''<!doctype html>
<html class="l-en" lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t_en}</title>
<meta name="title-fr" content="{t_fr}"><meta name="title-en" content="{t_en}">
<meta name="description" content="{d_en}">
<meta property="og:title" content="{t_en}"><meta property="og:description" content="{d_en}">
<meta property="og:image" content="https://sweatygame.com/img/hero-wide-8.jpg">
<meta name="theme-color" content="#121016">
<meta name="apple-itunes-app" content="app-id=6825698984">
<link rel="icon" href="img/favicon.png"><link rel="apple-touch-icon" href="img/icon.png">
<link rel="stylesheet" href="style.css?v={CSSV}">
<script src="lang.js?v={JSV}"></script>
</head>
<body>
'''

def bar():
    return f'''<div class="wrap bar">
  <a class="logo" href="./" aria-label="Sweaty"><img src="img/wordmark.png" alt="Sweaty" width="600" height="184"></a>
  <nav>
    <a class="hide-s" href="support.html">{F("Aide","Support")}</a>
    <a class="hide-s" href="privacy.html">{F("Confidentialité","Privacy")}</a>
    <a class="hide-s" href="terms.html">{F("Conditions","Terms")}</a>
    <span class="langs" role="group" aria-label="Language"><button data-set="fr" lang="fr">FR</button><button data-set="en" lang="en">EN</button></span>
  </nav>
</div>'''

FOOT = f'''<footer><div class="wrap row">
  <span>© <span id="y">2026</span> Sweaty · Matthias Sobrio</span>
  <nav>
    <a href="./">{F("Accueil","Home")}</a>
    <a href="support.html">{F("Aide et contact","Support")}</a>
    <a href="privacy.html">{F("Confidentialité","Privacy Policy")}</a>
    <a href="terms.html">{F("Conditions d'utilisation","Terms of Use")}</a>
  </nav>
</div></footer>
</body>
</html>
'''

def store():
    return f'''<span class="store" aria-label="App Store">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2zm0 3v13h10V5H7zm5 14.2a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/></svg>
  <span><small>{F("Bientôt sur","Coming soon to")}</small><b>{F("l’App Store","the App Store")}</b></span>
</span>'''

# ---------------- index ----------------
index = head("Sweaty · Le party game qui fait suer", "Sweaty · The party game that makes you sweat",
             "Des défis sportifs entre potes, sur un seul téléphone. 2 à 10 joueurs.", "Workout dares with friends, on a single phone. 2 to 10 players.") + f'''
<header class="hero">
  <picture>
    <source media="(max-width:860px)" srcset="img/hero-phone-8.jpg">
    <img class="bg" src="img/hero-wide-8.jpg" alt="" width="2000" height="1763">
  </picture>
  {bar()}
  <div class="wrap hero-copy">
    <h1 class="display">{F('Le party game qui fait <span class="neon">suer.</span>','The party game that makes you <span class="neon">sweat.</span>')}</h1>
    <p class="lead">{F("Un seul téléphone · 2 à 10 joueurs","One phone · 2–10 players")}</p>
    {store()}
  </div>
</header>

<section class="band ink">
  <div class="wrap">
    <h2 class="display">{F('Une soirée. <span class="neon">Un gagnant.</span>','One night. <span class="neon">One winner.</span>')}</h2>
    <p class="sub">{F("Une carte tombe, tu la joues devant tout le monde, le téléphone compte les points. Face-à-face, records, tenues où le premier qui craque a perdu.","A card comes up, you play it in front of everyone, the phone keeps score. Face-offs, records, holds where the first to crack loses.")}</p>
    <div class="gallery" data-l="fr"><figure class="tile"><figcaption><b class="display">Bats le<br><span class="neon">record.</span></b><span class="cap">76 défis express</span></figcaption><div class="phone"><img src="img/cap-fr-4.jpg" alt="Record de la maison battu par Léa" width="620" height="1348" loading="lazy"></div></figure><figure class="tile"><figcaption><b class="display">Le gagnant<br>prend <span class="neon">tout.</span></b><span class="cap">Le podium à partager en story</span></figcaption><div class="phone"><img src="img/cap-fr-5.jpg" alt="Podium de fin de partie" width="620" height="1348" loading="lazy"></div></figure><figure class="tile"><figcaption><b class="display">Du fou rire<br>au vrai <span class="neon">sport.</span></b><span class="cap">Choisis l’ambiance de la soirée</span></figcaption><div class="phone"><img src="img/cap-fr-6.jpg" alt="Les soirées de Sweaty" width="620" height="1348" loading="lazy"></div></figure><figure class="tile"><figcaption><b class="display">232 défis.<br><span class="neon">Zéro excuse.</span></b><span class="cap">Squats, pompes, gainage et plus</span></figcaption><div class="phone"><img src="img/cap-fr-7.jpg" alt="Choix des défis express" width="620" height="1348" loading="lazy"></div></figure></div>
    <div class="gallery" data-l="en"><figure class="tile"><figcaption><b class="display">Beat the<br><span class="neon">record.</span></b><span class="cap">76 express dares</span></figcaption><div class="phone"><img src="img/cap-en-4.jpg" alt="House record beaten by Léa" width="620" height="1348" loading="lazy"></div></figure><figure class="tile"><figcaption><b class="display">Winner<br>takes <span class="neon">all.</span></b><span class="cap">Share the podium to your story</span></figcaption><div class="phone"><img src="img/cap-en-5.jpg" alt="End-of-game podium" width="620" height="1348" loading="lazy"></div></figure><figure class="tile"><figcaption><b class="display">From silly to<br>seriously <span class="neon">sweaty.</span></b><span class="cap">Pick the vibe for the night</span></figcaption><div class="phone"><img src="img/cap-en-6.jpg" alt="Sweaty game nights" width="620" height="1348" loading="lazy"></div></figure><figure class="tile"><figcaption><b class="display">232 dares.<br><span class="neon">Zero excuses.</span></b><span class="cap">Squats, push-ups, planks and more</span></figcaption><div class="phone"><img src="img/cap-en-7.jpg" alt="Picking express dares" width="620" height="1348" loading="lazy"></div></figure></div>
    <p class="hint">{F("Fais défiler →","Scroll →")}</p>
  </div>
</section>

<section class="band ink" style="padding-top:8px">
  <div class="wrap">
    <div class="facts">
      <div class="fact"><b>232</b>{F("défis illustrés, du fou rire au vrai sport","illustrated dares, from silly to seriously sweaty")}</div>
      <div class="fact"><b>76</b>{F("défis express quand on n'a que cinq minutes","express dares for when you only have five minutes")}</div>
      <div class="fact"><b>2–10</b>{F("joueurs sur un seul téléphone","players on a single phone")}</div>
    </div>
  </div>
</section>

<section class="ink closing">
  <div class="wrap">
    <div class="mascots" aria-hidden="true">
      <img src="img/m-jumpingjack.webp" alt="" loading="lazy"><img src="img/m-dance.webp" alt="" loading="lazy"><img src="img/m-armwrestle.webp" alt="" loading="lazy"><img src="img/m-climber.webp" alt="" loading="lazy"><img src="img/m-chill.webp" alt="" loading="lazy">
    </div>
    <h2 class="display">{F('Pas de compte. Pas de matériel. <span class="neon">Zéro excuse.</span>','No account. No gear. <span class="neon">Zero excuses.</span>')}</h2>
    {store()}
  </div>
</section>
''' + FOOT

def doc(t_fr, t_en, h_fr, h_en, body_fr, body_en, dated=True):
    sub = F(f"Dernière mise à jour : {UPDATED_FR}", f"Last updated: {UPDATED_EN}", "p") if dated else F("On répond à chaque message.","We answer every message.","p")
    return head(t_fr, t_en, h_fr, h_en) + f'''<header class="doc-head">
  {bar()}
  <div class="wrap"><h1>{F(h_fr,h_en)}</h1>{sub}</div>
</header>
<main class="doc">
<div data-l="fr">{body_fr}</div>
<div data-l="en">{body_en}</div>
</main>
''' + FOOT

CONTACT_FR = '<div class="note green contact"><p style="margin:0 0 4px">Écris-nous :</p><a class="mail" href="#">contact</a></div>'
CONTACT_EN = '<div class="note green contact"><p style="margin:0 0 4px">Email us:</p><a class="mail" href="#">contact</a></div>'

# ---------------- privacy ----------------
PRIV_FR = f'''
<div class="note"><b>En bref.</b> Sweaty n'a pas de compte, pas de publicité et pas d'outil de mesure d'audience. Les prénoms et les photos des joueurs restent sur ton téléphone. Nous ne vendons aucune donnée.</div>
<h2>Qui sommes-nous</h2>
<p>Sweaty est une application éditée par Matthias Sobrio, développeur indépendant. Il est responsable du traitement des données décrites ici.</p>
<h2>Ce qui reste sur ton téléphone</h2>
<p>Pour faire tourner une partie, l'app enregistre localement, sur ton appareil uniquement :</p>
<ul>
<li>les prénoms des joueurs que tu saisis ;</li>
<li>les photos des joueurs et la photo du podium, si tu choisis d'en prendre ou d'en importer ;</li>
<li>tes réglages, tes records et l'avancement de tes parties.</li>
</ul>
<p>Ces données ne sont jamais envoyées sur nos serveurs. Nous n'en avons d'ailleurs pas. Elles restent sur l'appareil jusqu'à ce que tu retires un joueur, que tu changes une photo ou que tu supprimes l'app.</p>
<h2>Appareil photo et photothèque</h2>
<p>L'app te demande l'accès à l'appareil photo ou à tes photos seulement quand tu ajoutes une photo à un joueur ou au podium. C'est facultatif. Tu peux jouer sans photo et retirer l'autorisation à tout moment dans Réglages.</p>
<h2>Abonnement et achats</h2>
<p>Le paiement est géré par Apple. Nous ne voyons jamais tes coordonnées bancaires ni ton identifiant Apple.</p>
<p>Pour vérifier si ton abonnement est actif, l'app utilise RevenueCat, un prestataire de gestion d'abonnements. RevenueCat reçoit un identifiant aléatoire créé par l'app, sans lien avec ton nom, ainsi que l'historique de tes achats dans Sweaty, ton pays de boutique et des informations techniques comme la version de l'app et du système. Ces données servent uniquement à activer ce que tu as acheté et à restaurer tes achats. La politique de RevenueCat se trouve sur <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a>.</p>
<h2>Partage</h2>
<p>Quand tu appuies sur Partager, l'image de fin de partie est transmise à l'app que tu choisis, par exemple Instagram ou Messages. Rien n'est partagé sans ton geste. Ce que devient l'image ensuite dépend de la politique de cette app.</p>
<h2>Ce que nous ne faisons pas</h2>
<ul>
<li>Pas de compte ni de connexion.</li>
<li>Pas de publicité et pas de pistage entre apps ou sites.</li>
<li>Pas d'outil d'analyse d'audience.</li>
<li>Aucune vente ni location de données.</li>
</ul>
<h2>Enfants</h2>
<p>Sweaty ne s'adresse pas spécifiquement aux enfants de moins de 13 ans et ne collecte sciemment aucune donnée les concernant.</p>
<h2>Tes droits</h2>
<p>Comme nous ne conservons aucune donnée personnelle sur nos serveurs, la plupart de tes données sont entre tes mains : supprimer l'app les efface. Pour les données d'achat gérées par RevenueCat, tu peux nous demander leur accès ou leur suppression en nous écrivant. Tu peux aussi saisir la CNIL (cnil.fr) si tu estimes que tes droits ne sont pas respectés.</p>
<h2>Modifications</h2>
<p>Si cette politique change, nous mettrons à jour cette page et sa date.</p>
<div class="contact"><h2>Contact</h2>
<p>Une question sur tes données ?</p>
{CONTACT_FR}</div>
'''
PRIV_EN = f'''
<div class="note"><b>In short.</b> Sweaty has no accounts, no ads and no analytics. Player names and photos stay on your phone. We never sell data.</div>
<h2>Who we are</h2>
<p>Sweaty is published by Matthias Sobrio, an independent developer, who is the data controller for the processing described here.</p>
<h2>What stays on your phone</h2>
<p>To run a game, the app stores the following locally, on your device only:</p>
<ul>
<li>the player names you type in;</li>
<li>player photos and the podium photo, if you choose to take or import them;</li>
<li>your settings, records and game progress.</li>
</ul>
<p>This data is never sent to our servers. We don't run any. It stays on the device until you remove a player, change a photo or delete the app.</p>
<h2>Camera and photo library</h2>
<p>The app asks for camera or photo access only when you add a photo to a player or to the podium. It is optional. You can play without photos and revoke access at any time in Settings.</p>
<h2>Subscription and purchases</h2>
<p>Payment is handled by Apple. We never see your payment details or your Apple ID.</p>
<p>To check whether your subscription is active, the app uses RevenueCat, a subscription management provider. RevenueCat receives a random identifier created by the app, not linked to your name, along with your Sweaty purchase history, your store country and technical details such as app and OS version. This data is used only to unlock what you bought and to restore purchases. RevenueCat's policy is at <a href="https://www.revenuecat.com/privacy">revenuecat.com/privacy</a>.</p>
<h2>Sharing</h2>
<p>When you tap Share, the end-of-game image is handed to the app you pick, such as Instagram or Messages. Nothing is shared without your action. What happens to the image next is governed by that app's policy.</p>
<h2>What we don't do</h2>
<ul>
<li>No accounts or sign-in.</li>
<li>No ads and no tracking across apps or websites.</li>
<li>No analytics.</li>
<li>No selling or renting of data.</li>
</ul>
<h2>Children</h2>
<p>Sweaty is not directed at children under 13 and does not knowingly collect any data about them.</p>
<h2>Your rights</h2>
<p>Since we keep no personal data on our servers, most of your data is in your hands: deleting the app erases it. For purchase data held by RevenueCat, you can ask us for access or deletion by email. If you are in the EU, you may also lodge a complaint with your data protection authority.</p>
<h2>Changes</h2>
<p>If this policy changes, we will update this page and its date.</p>
<div class="contact"><h2>Contact</h2>
<p>A question about your data?</p>
{CONTACT_EN}</div>
'''

# ---------------- terms ----------------
TERMS_FR = f'''
<div class="note"><b>Avant de jouer.</b> Sweaty propose des exercices physiques. Joue à ton rythme, dans un espace dégagé, et arrête dès que quelque chose fait mal.</div>
<h2>L'application</h2>
<p>Sweaty est un jeu de soirée qui propose des défis sportifs à plusieurs, sur un seul téléphone. Elle est éditée par Matthias Sobrio. En utilisant l'app, tu acceptes ces conditions ainsi que le <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">contrat de licence standard d'Apple</a> pour les apps achetées sur l'App Store.</p>
<h2>Santé et sécurité</h2>
<ul>
<li>Sweaty est un jeu, pas un programme d'entraînement ni un avis médical.</li>
<li>Consulte un médecin avant de jouer si tu as un problème de santé, une blessure, si tu es enceinte ou si tu n'as pas fait de sport depuis longtemps.</li>
<li>Échauffe-toi, dégage l'espace autour de toi et joue sur un sol stable.</li>
<li>Arrête immédiatement en cas de douleur, de vertige ou d'essoufflement inhabituel.</li>
<li>Personne n'est obligé de faire un défi. Chacun choisit ses limites, et les autres les respectent.</li>
<li>Les mineurs jouent sous la surveillance d'un adulte.</li>
</ul>
<p>Tu joues sous ta propre responsabilité. Dans la limite permise par la loi, l'éditeur ne peut être tenu responsable des blessures ou des dommages liés à la pratique des défis.</p>
<h2>Abonnement Sweaty Pro</h2>
<p>Une partie de l'app est gratuite. L'abonnement Sweaty Pro débloque toutes les ambiances, les parties longues et tous les exercices express. Il est proposé à la semaine ou à l'année, au prix affiché dans l'app avant l'achat.</p>
<ul>
<li>Le paiement est débité sur ton compte Apple à la confirmation de l'achat.</li>
<li>L'abonnement se renouvelle automatiquement, sauf si tu le résilies au moins 24 heures avant la fin de la période en cours.</li>
<li>Le renouvellement est facturé dans les 24 heures précédant la fin de la période, au même prix.</li>
<li>Quand un essai gratuit est proposé, il ne concerne que l'offre annuelle. Sans résiliation au moins 24 heures avant sa fin, il se transforme en abonnement payant. La partie non utilisée d'un essai est perdue à l'achat d'un abonnement.</li>
<li>Tu gères et résilies ton abonnement dans Réglages, puis ton nom, puis Abonnements.</li>
<li>Les remboursements sont traités par Apple, sur <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
</ul>
<h2>Contenu</h2>
<p>Les textes, illustrations, personnages et le logo de Sweaty sont protégés. Tu peux partager les images de fin de partie générées par l'app, mais pas réutiliser le contenu de l'app à des fins commerciales.</p>
<h2>Évolution de l'app</h2>
<p>Nous pouvons faire évoluer l'app, ses défis et ses offres. Ces conditions peuvent aussi changer : la date en haut de la page indique la dernière version.</p>
<h2>Droit applicable</h2>
<p>Ces conditions sont soumises au droit français, sans préjudice des droits que te donne la loi de ton pays de résidence.</p>
<div class="contact"><h2>Contact</h2>
{CONTACT_FR}</div>
'''
TERMS_EN = f'''
<div class="note"><b>Before you play.</b> Sweaty involves physical exercise. Go at your own pace, in a clear space, and stop as soon as something hurts.</div>
<h2>The app</h2>
<p>Sweaty is a party game of group workout challenges played on one phone. It is published by Matthias Sobrio. By using the app, you accept these terms and <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple's Standard License Agreement</a> for apps obtained from the App Store.</p>
<h2>Health and safety</h2>
<ul>
<li>Sweaty is a game, not a training program or medical advice.</li>
<li>Check with a doctor before playing if you have a health condition or injury, are pregnant, or haven't exercised in a long time.</li>
<li>Warm up, clear the space around you and play on stable ground.</li>
<li>Stop immediately if you feel pain, dizziness or unusual shortness of breath.</li>
<li>No one has to take on a challenge. Everyone sets their own limits, and the others respect them.</li>
<li>Minors play under adult supervision.</li>
</ul>
<p>You play at your own risk. To the extent permitted by law, the publisher is not liable for injuries or damage arising from the challenges.</p>
<h2>Sweaty Pro subscription</h2>
<p>Part of the app is free. A Sweaty Pro subscription unlocks every game mood, longer games and all express exercises. It is offered weekly or yearly, at the price shown in the app before purchase.</p>
<ul>
<li>Payment is charged to your Apple account when you confirm the purchase.</li>
<li>The subscription renews automatically unless cancelled at least 24 hours before the end of the current period.</li>
<li>Renewal is charged within 24 hours before the end of the period, at the same price.</li>
<li>When a free trial is offered, it applies to the yearly plan only. Unless cancelled at least 24 hours before it ends, it turns into a paid subscription. Any unused part of a trial is forfeited when you buy a subscription.</li>
<li>Manage or cancel your subscription in Settings, then your name, then Subscriptions.</li>
<li>Refunds are handled by Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</li>
</ul>
<h2>Content</h2>
<p>Sweaty's texts, illustrations, characters and logo are protected. You may share the end-of-game images the app creates, but not reuse the app's content commercially.</p>
<h2>Changes to the app</h2>
<p>We may change the app, its challenges and its offers. These terms may change too: the date at the top shows the latest version.</p>
<h2>Governing law</h2>
<p>These terms are governed by French law, without prejudice to the rights granted by the law of your country of residence.</p>
<div class="contact"><h2>Contact</h2>
{CONTACT_EN}</div>
'''

# ---------------- support ----------------
def qa(q, a): return f'<details><summary>{q}</summary><p>{a}</p></details>'
SUP_FR = f'''
{CONTACT_FR}
<p>Un bug, une idée de défi, un souci d'abonnement : décris-nous ce qui se passe, avec ton modèle d'iPhone si c'est un bug.</p>
<h2>Questions fréquentes</h2>
<div class="faq">
{qa("Comment on joue ?","Ajoute les joueurs, choisis une ambiance et pose le téléphone là où tout le monde le voit. Une carte tombe : solo, face-à-face, record ou tous ensemble. On joue, le téléphone compte les points, et le podium tombe à la fin.")}
{qa("Combien de joueurs ?","De 2 à 10, sur un seul téléphone. Pas besoin que chacun installe l'app.")}
{qa("Faut-il du matériel ?","Non. Un peu de place suffit. Certains défis utilisent un mur ou une chaise.")}
{qa("Où vont les photos des joueurs ?","Elles restent sur ton téléphone. Rien n'est envoyé sur internet, sauf si tu partages toi-même l'image de fin de partie.")}
{qa("J'ai changé de téléphone, comment récupérer mon abonnement ?","Ouvre l’écran d’abonnement et touche « Restaurer un achat », avec le même identifiant Apple que pour l'achat.")}
{qa("Comment résilier mon abonnement ?","Sur ton iPhone : Réglages, puis ton nom, puis Abonnements, puis Sweaty. Résilie au moins 24 heures avant le renouvellement.")}
{qa("Comment obtenir un remboursement ?","Les paiements passent par Apple. Fais ta demande sur reportaproblem.apple.com.")}
{qa("Comment effacer mes données ?","Retire les joueurs dans l'app, ou supprime l'app : tout ce qu'elle a enregistré disparaît avec elle.")}
</div>
<p style="margin-top:28px">Voir aussi la <a href="privacy.html">politique de confidentialité</a> et les <a href="terms.html">conditions d'utilisation</a>.</p>
'''
SUP_EN = f'''
{CONTACT_EN}
<p>A bug, a challenge idea, a subscription issue: tell us what happened, with your iPhone model if it's a bug.</p>
<h2>FAQ</h2>
<div class="faq">
{qa("How do you play?","Add the players, pick a mood and set the phone where everyone can see it. A card comes up: solo, face-off, record or all together. You play, the phone keeps score, and the podium comes at the end.")}
{qa("How many players?","From 2 to 10, on a single phone. Nobody else needs to install the app.")}
{qa("Do I need any equipment?","No. A bit of room is enough. Some challenges use a wall or a chair.")}
{qa("Where do player photos go?","They stay on your phone. Nothing is uploaded, unless you share the end-of-game image yourself.")}
{qa("I got a new phone. How do I get my subscription back?","Open the subscription screen and tap “Restore a purchase”, signed in with the Apple ID you bought with.")}
{qa("How do I cancel my subscription?","On your iPhone: Settings, then your name, then Subscriptions, then Sweaty. Cancel at least 24 hours before renewal.")}
{qa("How do I get a refund?","Payments go through Apple. Request one at reportaproblem.apple.com.")}
{qa("How do I delete my data?","Remove the players in the app, or delete the app: everything it stored goes with it.")}
</div>
<p style="margin-top:28px">See also the <a href="privacy.html">Privacy Policy</a> and the <a href="terms.html">Terms of Use</a>.</p>
'''

pages = {
 "index.html": index,
 "privacy.html": doc("Sweaty · Confidentialité","Sweaty · Privacy Policy","Politique de confidentialité","Privacy Policy",PRIV_FR,PRIV_EN),
 "terms.html": doc("Sweaty · Conditions d'utilisation","Sweaty · Terms of Use","Conditions d'utilisation","Terms of Use",TERMS_FR,TERMS_EN),
 "support.html": doc("Sweaty · Aide et contact","Sweaty · Support","Aide et contact","Support",SUP_FR,SUP_EN,dated=False),
}
pages['index.html']=pages['index.html'].replace('<body>','<body class="home">',1)
for n, html in pages.items():
    (OUT/n).write_text(html, encoding="utf-8")
print("written", list(pages))
