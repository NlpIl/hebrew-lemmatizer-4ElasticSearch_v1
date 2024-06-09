# hebrew-lemmatizer

<div dir="rtl">

## אמל"ק

במסגרת תכנית ה NLP הלאומית פיתחו Korra.ai ומפא"ת פלאגין לחיפוש בעברית לElasticsearch-. הפלאגין מבוסס על מודל למטיזציה של Dictabert, יחד עם אלגוריתם להורדת Stopwords. הפלאגין והמודל מפורסמים לציבור לשימוש חופשי.

## רקע

בנית פלטפורמה לחיפוש בעברית וערבית היא חלק מתכנית ה NLP הלאומית בעברית וערבית.

<https://nnlp-il.mafat.ai/#Our-Github>

&nbsp;במסגרת זו, מובילה מפא"ת תכנית הכוללת מספר רב של פרויקטים.  מטרת התכנית היא לפתח אבני יסוד תשתיתיות לעיבוד שפות טבעיות ולהעמיד אותן לרשות קהילת העוסקים בתחום. העבודה המאסיבית על משאבי-יסוד תביא לפיתוח מואץ של יישומי קצה.  אבני היסוד כוללות בניית מאגרי מידע מתוייגים, מודל שפה ענק (LLM), ופיתוח יכולות ושירותים מתקדמים בעברית וערבית בקוד פתוח (open source) כשירות למדענים, ארגונים ממשלתיים וחברות מסחריות. פרויקט החיפוש בעברית הוא נדבך חשוב מתוך כלל המשאבים, ומהווה תרומה קריטית למשאבים הציבוריים שניתנים לכול ללא עלות.

המערכת הנפוצה ביותר לחיפוש היא Elasticsearch ("אלסטיק"), וארגונים רבים בישראל ובעולם, משתמשים בה לחיפוש תוך- וחוץ- ארגוני . אלסטיק נוצרה כפלטפורמת קוד פתוח ובבסיסה עומד אלגוריתם 25BM אשר מממש נוסחה סטטיסטית לאחזור מסמכים לפי תדירות הופעת מילות מפתח בהם. עם מהפכת ה-AI חברת אלאסטיק הוסיפה גם אפשרות לחיפוש וקטורי והוספת מודלים נוירונלים, כדי להמשיך ולשמר את מעמד הפלטפורמה כפתרון הסטנדרטי לחיפוש.

האם לאחר מהפכת ה-AI יש צורך בחיפוש מבוסס מילות מפתח? התשובה היא חיובית. ראשית, מילים רבות הינן ספציפיות לתחום ידע מסוים או לארגון מסוים, ולפיכך אין מודל אשר מכיר אותן. זו בעיה הקיימת ביחוד בחיפוש תוך ארגוני. שנית, מתוך נסיון, המודלים הנוירונליים בעברית עדיין אינם בוגרים דיים ויש עדיין צורך בתמיכה של מילות מפתח.

מהי למטיזציה ומדוע יש בה צורך? למטיזציה דומה להוצאת שורש למילה. בפעלים, הלמטיזציה הופכת אותם לגוף שלישי יחיד, למשל הולכים – הולך. בשמות עצם הלמטיזציה מעבירה ליחיד: נשים – אשה. בעולם החיפוש משתמשים בה כדי לנרמל את שאלת החיפוש ואת המסמכים נשואיו לאותו בסיס. למשל, אם השאלה היא "באילו בניינים הותקנו צינורות ברזל", למטיזציה תאפשר לאחזר מסמכים המכילים משפטים כגון "בבנין 17 מותקן צינור ברזל".

מהן הבעיות שיש לפתור בבואנו לבצע למטיזציה? שפות כמו עברית וערבית הן שפות עשירות מבחינה מורפולוגית, מכך נובעות שתי בעיות עיקריות. ראשית, בכל מילה חבויות מספר מילים. למשל המילה "שבבתיהם" במשפט "האזרחים שבבתיהם מותקן צינור ברזל" תתורגם בשפה האנגלית ל-that inside their homes - הווה אומר, ארבע מילים חבויות בתוך מילה אחת! בנוסף לכך, מאחר ורוב המסמכים בישראל הינם ללא ניקוד, הבנת המילה תלויה לחלוטין בהקשר. למשל, המילה "שמן" יכולה להיות, became fat their name, oil, their oil, fat, from which – שש אפשרויות שונות.

במשך השנים פותחו מספר פיתרונות לבעיה – החל מ[שימוש במילון](http://hspell.ivrix.org.il/) ועד למודל [למידת מכונה](https://github.com/OnlpLab/yap). לאחרונה, הוציאה עמותת דיקטה מודל נוירונלי, המבוסס על Dictabert, מודל הבסיס שפתחו. בפרויקט זה לקחנו מודל זה ובנינו לו ממשק שמאפשר עבודה שלו עם אלסטיק. ניתן לקרוא על המודל [כאן](https://dicta.org.il/developers).

הורדת ה-stopwords מתבצעת כדי לנטרל השפעה של מילים נפוצות מדי שאין להן משמעות בחיפוש נוירונלי, כגון "אז" "אם" "לא" וכו'. לצורך כאן בצענו ניתוח סטטיסטי של מספר קורפוסים שונים, ובחרנו מהם את המילים הנפוצות ביותר.

### ארכיטקטורה
![Architecture](/architecture.png)


הלמטיזציה מתבצעת בשני זמנים: בזמן אינדוקס ובזמן חיפוש. בשני זמנים אלו התהליך זהה. אלסטיק מעביר את הטקסט אל הפלאגין, וזה בתורו קורא לקונטיינר שמריץ בתוכו תכנית פייתון המעבירה את הטקס למודל, ומקבלת אותו בחזרה בתור למות. לאחר מכן, מתבצעת מחיקת stop words והטוקנים הנותרים מועברים לאלסטיק להמשך שרשרת הביצוע.

כאמור, למודל יש מספר גרסאות ואנו ערכנו בדיקות דיוק ובדיקות מהירות בתצורות שונות, למודל ה-TINY, המאפשר הרצה על שרת רגיל ללא צורך בGPU. קיבלנו בהן את הערכים [הבאים]([url](https://drive.google.com/file/d/16DBh0EFsnIkTPvLKvZEOGhAyMuT2Tatj/view)):
[
טבלת הבדיקות
](https://drive.google.com/file/d/16DBh0EFsnIkTPvLKvZEOGhAyMuT2Tatj/view)
אורך ה-batch המקסימלי הינו 512 תווים.

דף הדגמה ונסיון נמצא [כאן]([url](http://heb.korra.ai:8080/)): http://heb.korra.ai:8080/
<div dir="rtl">
## הוראות התקנה ושימוש:<div dir="rtl">
1. בצע git clone לרפוזיטורי זה<div dir="rtl">
2. יש להריץ git lfs pull 
<div dir="rtl">
3. כדי להריץ Dicta במכונה אחרת או בקונטיינר שאינו מאזין על ברירת המחדל (שהינה http://dicta:8000) יש להגדיר על המכונה משתנה סביבה בשם KORRA_HEB_URL שהערך שלו מהצורה "http://IP:Port/lemmas" .יש לוודא שברגע שמחליטים להשתמש ב port שונה מ 8000 צריך לחליף את ה Port בDOCKETFILE שיוצר את DICTA (תחת תיקיית dicta)  לאותו ה-Port אשר הגדרנו ב KORRA_HEB_URL. <BR> לצורך ההגדרה אפשר ליצור או להוסיף לקובץ בשם 
/etc/environment את הגדרת KORRA_HEB_URL
<div dir="rtl">
4. הרץ את install.sh מתוך bash <div dir="rtl">
 <div dir="rtl">
5. הרצה זו מריצה שני קונטיינרים המוגדרים ב-docker-compose.yml <div dir="rtl">
 <div dir="rtl">
קובץ זה יעלה שני קונטיינרים:
<BR/>
 א dicta - אחראי על חלקות הטקסט למשפטים ושליחת batches בגודל 16 . אפשר לשנות את הגודל בקובץ dicta/src/lemmatization.py
<BR/>
 ב es0 - קונטיינר המריץ Elasticsearch עם  node בודד. ניתן להשתמש ביותר מ node אחד כמובן.
<BR/><BR/>
6. לבדיקה, מצורפת דוגמת שימוש בקובץ plugin_test.py.

<div dir="rtl">
## הוראות שינוי גרסה:
1.יש לוודא שמותקן JDK . מומלץ להשתמש בגרסה 19 וגם gradle גרסה 8.4 
2. צריף לשנות את גרסת אלסטיק במקומות הבאים:
א. ב-Dockerfile שב elasticsearch
ב. ב-plugin-lemmas
/build.gradle
ג. plugin-stopwords
/build.gradle

2.יש לבנות את הפלאגין stopwords ו lemmas כדי לחבר אותם לElastic ע"י הרצת build.sh . 

#### הערות:
<div dir="rtl">
1. יש לוודא של git lfs מותקן לפני ה-clone.
<div dir="rtl">
2. גודל JVM ב docker-compose.yml הוא 512M אבל אפשר להגדיל אותו עבור מחשבים חזקים.
   <div dir="rtl">
3. מודל dicta-tiny מבוסס על cpu לכן ככל שמקצים לו יותר cpu זמן העיבוד הולך וקטן. עם זאת, מנסיוננו הוספת מעבדים מעל 8 אינה משפרת את המהירות.
   <div dir="rtl">
4.  במידה ולא משתמשים בbuild.sh  אלא מריצים את אלאסטיק ישירות על המכונה, יש לבצע מספר שינויים לתהליך המתואר לעיל:
   * יש להתקין את הפלאגין ידנית ע"י העתקתו והרצת סקריפט התקנה (ניתן לראות את הפעולות בתוך הDOCKERFILE של es01)
   * יש לעדכן את כתובת הDICTA בשני מקומות: גם כמשתנה סביבה וגם בתוך הקובץ plugin.policy אשר מצוי בתוך תיקיית /usr/share/elastic/jdk/conf/securit.  

### התקנה בעזרת Images:

1. העתיקו את הקובץ docker-compose-images.yml
2. צרו את התיקיות data/elastic ו- models/huggingface
3. הריצו docker compose -f docker-compose-images.yml build 
4. הריצו docker compose -f docker-compose-images.yml up -d
5. ניתן לוודא שהפלאגין עובד ע"י

curl -X GET "http://localhost:9200/_analyze?pretty" -H "Content-Type: application/json" -d '{
    "text": "חידושים כמו חיבור אינטרנט אלחוטי,טלפוניה ניידת, ושירותי ענן משנים את הפנייה שלנו אל העולם.",
    "tokenizer": "whitespace",
    "filter": ["heb_lemmas", "heb_stopwords"]
    }'

   
   
