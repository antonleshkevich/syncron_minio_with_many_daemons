Установка:
1. Запустите сервер minio
2.<h3>Необязательно</h3>: <p>Пожалуйста, поместите на сервер любой файл и запустите программу "testtime.py" с сигнатурой:./testtime.py quit q --s3 HOST_NAME --access_key ACCESS_KEY --secret_key SECRET_KEY --dir DIR_NAME --bucket BUCKET_NAME; и посмотрите результат времени, если время отличается на -3 часа (как собственно у меня на компьютере), то можете приступать к использованию основной программы. Если время не отличается, откройте файл miniovar.py и закоментируйте строку 274 (есть отметка) и в строке 278 перед сигнатуру dt2[0:-13] поменяйте на сигнатуру str(dt2)[0:-13]. Если вам лень это сделать или же просто боитесь испортить программу, сообщите об этой проблеме автору программы (antonleshkevich), и я постараюсь вернуть вам рабочую для вашей системы версию :)</p>
3.</h3>Пожалуйста, создайте в папке с программой файл "database"<.h3>
<p>Использование:</p>
1. <p> Запуск программы: nohup ./daemon.py quit q --s3 HOST_NAME --access_key ACCESS_KEY --secret_key SECRET_KEY --dir ~/a --bucket BUCKET_NAME &</p>
<p>В файле nohup.out храняться все логи программы. Рекомендуется переодически очищать его.</p>
<p>Внимание, при неверное работе программы, попробуйте сменить в файле daemon.py 8 строчку с miniovar.reallyrun() на miniovar.run()</p>
