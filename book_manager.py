#-*- coding:cp949 -*- <--�ѱ��� ������ϱ� ���� ���ڵ��� cp949�� ���
# ���� ����1 : �������� ���α׷�


class State():
	cont = 1
	end = 2


def show_menu():
    print '''
1) ���ο� ���� �Է�
2) ��ü ������� ���
3) ���� ����
4) ���� �˻�
5) ���� ���� �� ������
'''
    return raw_input('�޴� ���� --> ')


class FileManger:
	def __init__(self, file_name):
		self.file_name = file_name
		self.file = ''

	def get_all(self):
		with open(self.file_name,'r') as fi:
			return fi.read()
	def get_all_lines(self):
		with open(self.file_name,'r') as fi:
			return fi.read().split('\n')

	def get_reader(self):
		self.file = open(self.file_name,'r')
		return self.file

	def get_last_lines(self):
		if self.file != '' and self.file.mode == 'w': self.file = open(self.file_name,'r')
		else: self.file = open(self.file_name,'r')
		return self.file.read().split('\n')[-1]

	def insert_line(self, line):
		if self.file != '' and self.file.mode == 'r': self.file = open(self.file_name,'a')
		else: self.file = open(self.file_name,'a')
		self.file.write(line)

	def write(self, line):
		if self.file != '' and self.file.mode == 'r': self.file = open(self.file_name,'w')
		if self.file != '' and self.file.mode == 'w': self.file = open(self.file_name,'a')
		if self.file == '' : self.file = open(self.file_name,'w')
		self.file.write(line)


class BookManger(FileManger):
	def __init__(self,file_name):
		self.book_dict = dict()
		FileManger.__init__(self,file_name)
		self.file2Dict()

	def file2Dict(self):
		for line in FileManger.get_all_lines(self):
			if line == '': continue
			datas = line.split('\t')
			self.book_dict[datas[0]] = {
				"title" : datas[1],
				"author" : datas[2],
				"published_date" : datas[3]
			}


	def insert_book(self):
		title = raw_input("\ntitle : ")
		author = raw_input("\nauthor : ")
		published_date = raw_input("\npublished_dated : ")
		last_index = max(self.book_dict.keys())
		new_index = str(int(last_index) + 1)
		self.book_dict[new_index] = {
			"title" : title,
			"author" : author,
			"published_date" : published_date
		}

	def delete_book(self):
		index = raw_input("\n������� �ϴ� å�� ��ȣ�� �����ּ��� : ")
		try:
			del self.book_dict[index]
		except:
			print "������� �ϴ� å�� �����ϴ�."

	def find_book(self):
		target_column = raw_input("\nã���� �ϴ� ������ �����ּ��� : ")

		target_item = raw_input("\nã���� �ϴ� ���� �����Դϱ� ? : ")

		searched_dict = {k : v for k, v in self.book_dict.iteritems() if target_item in v[target_column] }
		
		for index in sorted(searched_dict.keys(), key = lambda x : int(x)):
			print "index : {} title : {} author : {} published_date : {}".format(index,
																				 searched_dict[index]['title'],
																				 searched_dict[index]['author'],
																				 searched_dict[index]['published_date']
																				 )

	def print_all_book(self):
		indexs = sorted(self.book_dict.keys(), key = lambda x : int(x))
		for index in indexs:
			print "index : {} title : {} author : {} published_date : {}".format(index,
																				 self.book_dict[index]['title'],
																				 self.book_dict[index]['author'],
																				 self.book_dict[index]['published_date']
																				 )

	def save(self):
		for index in sorted(self.book_dict.keys(), key = lambda x : int(x)):
			FileManger.write(self,"\t".join([index, self.book_dict[index]['title'], self.book_dict[index]['author'], self.book_dict[index]['published_date']]) + '\n')
		return State.end

def dispachter(menu_num):
	global bm
	if menu_num == '1': return bm.insert_book()
	if menu_num == '2': return bm.print_all_book()
	if menu_num == '3': return bm.delete_book()
	if menu_num == '4': return bm.find_book()
	if menu_num == '5': return bm.save()

if __name__ == '__main__':
	bm = BookManger('books.txt')
	while(True):
		if dispachter(show_menu()) == State.end:		
			break



        
