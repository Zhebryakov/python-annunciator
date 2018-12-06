# python-annunciator
files annunciator in directory YY/MM/DD
program list current day directory (YYMMDD) in directory main_dir. if new file exist in directory   - script  put his name in file
spisok.txt and send message 

скрипт в директории main_dir читает подкаталог YYMMDD, соответствующий текущему дню. при появлении в данном каталоге нового файла,
его имя добавляется в файл spisok.txt в данном подкаталоге и происходит рассылка извещений по списку адресов toadr=["person1@domen.ru","person2@domen.ru"]
