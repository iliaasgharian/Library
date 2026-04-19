import model
import sqlite3
import datetime


connection = sqlite3.connect("NewLibrary.db")
cursor = connection.cursor()


class CategoryDataAdapter:

    @staticmethod
    def get_all():
        table = list(cursor.execute("SELECT * FROM categories;"))
        return [model.Category(row[0], row[1]) for row in table]

    def insert(category: model.Category):
        cursor.execute(
            "INSERT INTO categories (`name`) VALUES ('{}');".format(category.name))
        connection.commit()
        a = cursor.lastrowid
        return model.Category(a, category.name)

    def delete(id: int):
        n = cursor.execute("Select * from categories where id=={}".format(id))
        if len(list(n)) == 0:
            return False
        else:
            s = cursor.execute(
                "Select * from book_category where category_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from categories where id=={}".format(id))
                connection.commit()
                return True
            else:
                return False

    @staticmethod
    def search(name: str):
        s = cursor.execute(
            "Select * from categories where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(model.Category(i[0], i[1]))
        return lis


class AuthorDataAdapter:
    @staticmethod
    def update(id:int,name:str,birthdate: datetime.date,nationality:str):
        
        s = cursor.execute("""Update authors
                                   SET name='{}',birthdate='{}',nationality='{}'
                                   where id={};""".format(name,str(birthdate),nationality,id))
        connection.commit()
        return 
        
    @staticmethod
    def get_one(id: int):
        s = cursor.execute("Select * from authors where id=={}".format(id))
        lis = []
        for i in s:
            lis.append(model.Author(i[0], i[1], i[2], i[3]))
        return lis

    @staticmethod
    def get_all():
        table = list(cursor.execute("SELECT * FROM authors;"))
        return [model.Author(row[0], row[1], datetime.date.fromisoformat(row[2]), row[3]) for row in table]

    @staticmethod
    def delete(id: int):
        s = cursor.execute("Select * from authors where id=={}".format(id))
        if len(list(s)) == 0:
            return False
        else:
            s = cursor.execute(
                "Select author_id from book_author where author_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute("Delete from authors where id=={}".format(id))
                connection.commit()
                return True
            else:
                return False

    def insert(author: model.Author):
        cursor.execute("INSERT INTO authors (`name`,`birthdate`,`nationality`) VALUES ('{}','{}','{}');".format(
            author.name, author.birthdate, author.nationality))
        connection.commit()
        a = cursor.lastrowid
        return model.Author(a, author.name, author.birthdate, author.nationality)

    @staticmethod
    def search(name: str):
        s = cursor.execute(
            "Select * from authors where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(model.Author(i[0], i[1], i[2], i[3]))
        return lis


class PublisherDataAdapter:

    @staticmethod
    def get_all():
        table = list(cursor.execute("SELECT * FROM publishers;"))
        return [model.Publisher(row[0], row[1], row[2], row[3]) for row in table]

    def insert(publisher: model.Publisher):
        cursor.execute("INSERT INTO publishers (`name`,`address`,`website`) VALUES ('{}','{}','{}');".format(
            publisher.name, publisher.address, publisher.website))
        connection.commit()
        a = cursor.lastrowid
        return model.Publisher(a, publisher.name, publisher.address, publisher.website)

    def delete(id: int):
        n = cursor.execute("Select * from publishers where id=={}".format(id))
        if len(list(n)) == 0:
            return False
        else:
            s = cursor.execute(
                "Select publisher_id from books where publisher_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from publishers where id=={}".format(id))
                connection.commit()
                return True
            else:
                return False

    @staticmethod
    def search(name: str):
        s = cursor.execute(
            "Select * from publishers where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(model.Publisher(i[0], i[1], i[2], i[3]))
        return lis


class LanguageDataAdapter:
    @staticmethod
    def get_all():
        table = list(cursor.execute("SELECT * FROM languages;"))
        return [model.Language(row[0], row[1]) for row in table]

    def insert(language: model.Language):
        cursor.execute(
            "INSERT INTO languages (`name`) VALUES ('{}');".format(language.name,))
        connection.commit()
        a = cursor.lastrowid
        return model.Language(a, language.name)

    def delete(id: int):
        n = cursor.execute("Select * from languages where id=={}".format(id))
        if len(list(n)) == 0:
            return False
        else:
            s = cursor.execute(
                "Select * from book_language where language_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute("Delete from languages where id=={}".format(id))
                connection.commit()
                return True
            else:
                return False

    @staticmethod
    def search(name: str):
        s = cursor.execute(
            "Select * from languages where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(model.Language(i[0], i[1]))
        return lis


class DesignerDataAdapter:

    @staticmethod
    def get_all():
        table = list(cursor.execute("SELECT * FROM cover_designers;"))
        return [model.CoverDesigner(row[0], row[1], datetime.date.fromisoformat(row[2]), row[3]) for row in table]

    def insert(designer: model.CoverDesigner):
        cursor.execute("INSERT INTO cover_designers (`name`,`birthdate`,`nationality`) VALUES ('{}','{}','{}');".format(
            designer.name, designer.birthdate, designer.nationality))
        connection.commit()
        a = cursor.lastrowid
        return model.CoverDesigner(a, designer.name, designer.birthdate, designer.nationality)

    def delete(id: int):
        n = cursor.execute(
            "Select * from cover_designers where id=={}".format(id))
        if len(list(n)) == 0:
            return False
        else:
            s = cursor.execute(
                "Select * from book_designer where designer_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from cover_designers where id=={}".format(id))
                connection.commit()
                return True
            else:
                return False

    @staticmethod
    def search(name: str):
        s = cursor.execute(
            "Select * from cover_designers where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(model.CoverDesigner(i[0], i[1], i[2], i[3]))
        return lis


class TranslatorDataAdapter:

    @staticmethod
    def get_all():
        table = list(cursor.execute("SELECT * FROM translators;"))
        languages = LanguageDataAdapter.get_all()
        return [model.Translator(row[0], row[1], list(filter(lambda lang: lang.name == row[2], languages))) for row in table]

    def insert(translator: model.Translator):
        cursor.execute("INSERT INTO translators (`name`,`language`) VALUES ('{}','{}');".format(
            translator.name, translator.languages))
        connection.commit()
        a = cursor.lastrowid
        return model.Translator(a, translator.name, translator.languages)

    def delete(id: int):
        n = cursor.execute("Select * from translators where id=={}".format(id))
        if len(list(n)) == 0:
            return False
        else:
            s = cursor.execute(
                "Select * from book_translator where translator_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute(
                    "Delete from translators where id=={}".format(id))
                connection.commit()
                return True
            else:
                return False

    @staticmethod
    def search(name: str):
        s = cursor.execute(
            "Select * from translators where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(model.Translator(i[0], i[1], i[2]))
        return lis


class ResourcesDataAdapter:

    @staticmethod
    def get_all():
        table = list(cursor.execute("SELECT * FROM resources;"))
        return [model.Resources(row[0], row[1]) for row in table]

    def insert(resource: model.Resources):
        cursor.execute(
            "INSERT INTO resources (`name`) VALUES ('{}');".format(resource.name))
        connection.commit()
        a = cursor.lastrowid
        return model.Language(a, resource.name)

    def delete(id: int):
        n = cursor.execute("Select * from resources where id=={}".format(id))
        if len(list(n)) == 0:
            return False
        else:
            s = cursor.execute(
                "Select * from resources_book where resource_id=={}".format(id))

            if len(list(s)) == 0:
                cursor.execute("Delete from resources where id=={}".format(id))
                connection.commit()
                return True
            else:
                return False

    @staticmethod
    def search(name: str):
        s = cursor.execute(
            "Select * from resources where name like '%{}%'".format(name))
        lis = []
        for i in s:
            lis.append(model.Resources(i[0], i[1]))
        return lis


class BookDataAdapter:

    @staticmethod
    def get_all():
        sql = "SELECT id,title,product_code,age_group,publisher_id,release_date,price,author_id,category_id,designer_id,language_id,translator_id,resource_id from books LEFT JOIN book_author on book_author.book_id==books.id LEFT JOIN book_category on book_category.book_id==books.id LEFT JOIN book_designer on book_designer.book_id==books.id LEFT JOIN book_language on book_language.book_id==books.id LEFT JOIN book_translator on book_translator.book_id==books.id LEFT JOIN resources_book on resources_book.book_id==books.id "
        table = list(cursor.execute(sql))

        categories = CategoryDataAdapter.get_all()
        authors = AuthorDataAdapter.get_all()
        publishers = PublisherDataAdapter.get_all()
        languages = LanguageDataAdapter.get_all()
        cover_designers = DesignerDataAdapter.get_all()
        translators = TranslatorDataAdapter.get_all()
        resources = ResourcesDataAdapter.get_all()

        books = []
        for row in table:
            book_id = row[0]
            title = row[1]
            product_code = row[2]
            age_group = row[3]
            publisher = publishers[publishers.index(row[4])]
            release_date = datetime.date.fromisoformat(row[5])
            price = row[6]

            # book_categories = [categories[categories.index(cat)] for cat in [
            #     cat_row[7] for cat_row in table if cat_row[0] == book_id] if cat is not None and not cat in book_categories]
            book_categories = []

            for cat_row in table:

                if cat_row[0] == book_id and cat_row[8] is not None and cat_row[8] not in book_categories:

                    book_categories.append(
                        categories[categories.index(cat_row[8])])

        #     book_authors = [authors[authors.index(author)] for author in [
        #         author_row[8] for author_row in table if author_row[0] == book_id] if author is not None]
            book_authors = []

            for auth_row in table:

                if auth_row[0] == book_id and auth_row[7] is not None and auth_row[7] not in book_authors:

                    book_authors.append(authors[authors.index(auth_row[7])])

        #     book_languages = [languages[languages.index(language)] for language in [
        #         language_row[9] for language_row in table if language_row[0] == book_id] if language is not None]
            book_languages = []
            for lang_row in table:
                if lang_row[0] == book_id and lang_row[10] is not None and lang_row[10] not in book_languages:
                    book_languages.append(
                        languages[languages.index(lang_row[10])])

        #     book_designers = [cover_designers[cover_designers.index(designer)] for designer in [
        #         designer_row[10] for designer_row in table if designer_row[0] == book_id] if designer is not None]
            book_designers = []
            for des_row in table:
                if des_row[0] == book_id and des_row[9] is not None and des_row[9] not in book_designers:
                    book_designers.append(
                        cover_designers[cover_designers.index(des_row[9])])

        #     book_translators = [translators[translators.index(translator)] for translator in [
        #         translator_row[11] for translator_row in table if translator_row[0] == book_id] if translator is not None]
            book_translators = []
            for tran_row in table:
                if tran_row[0] == book_id and tran_row[11] is not None and tran_row[11] not in book_translators:
                    book_translators.append(
                        translators[translators.index(tran_row[11])])

        #     book_resources = [resources[resources.index(resource)] for resource in [
        #         resources_row[12] for resources_row in table if resources_row[0] == book_id] if resource is not None]
            book_resources = []
            for res_row in table:
                if res_row[0] == book_id and res_row[12] is not None and res_row[12] not in book_resources:
                    book_resources.append(
                        resources[resources.index(res_row[12])])

            books.append(model.Book(
                id=book_id,
                title=title,
                product_code=product_code,
                categories=book_categories,
                age_group=age_group,
                authors=book_authors,
                publisher=publisher,
                release_date=release_date,
                price=price,
                languages=book_languages,
                cover_designers=book_designers,
                translators=book_translators,
                resources=book_resources))
        newbooks = []
        for i in books:
            status = True
            for j in newbooks:
                if j.id == i.id:
                    status = False
            if status:
                newbooks.append(i)
        return newbooks

    def delete(id: int):
        n = cursor.execute("Select * from books where id=={}".format(id))
        if len(list(n)) == 0:
            return False
        else:
            cursor.execute(
                "Delete FROM book_author where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_category where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_language where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_designer where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM book_translator where book_id=={};".format(id))
            connection.commit()
            cursor.execute(
                "Delete FROM resources_book where book_id=={};".format(id))
            connection.commit()
            cursor.execute("Delete FROM books where id=={};".format(id))
            connection.commit()
            return True

    def insert(book: model.Book):

        title = book.title
        code = book.product_code
        cat = [book.categories[i].id for i in range(len(book.categories))]
        age_group = book.age_group
        release_date = book.release_date

        author = [book.authors[i].id for i in range(len(book.authors))]
        price = book.price

        language = [book.languages[i].id for i in range(len(book.languages))]
        publisher = book.publisher.id

        cover_designer = [book.cover_designers[i].id for i in range(
            len(book.cover_designers))]

        translator = [book.translators[i].id for i in range(
            len(book.translators))]

        resource = [book.resources[i].id for i in range(len(book.resources))]

        cursor.execute("INSERT INTO books (title, product_code,age_group, publisher_id, release_date, price) VALUES('{}', {}, '{}',{},'{}',{});".format(
            title, code, age_group, publisher, release_date, price))
        connection.commit()
        a = cursor.lastrowid
        for i in author:
            cursor.execute(
                "INSERT INTO book_author (`book_id`, `author_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in cat:
            cursor.execute(
                "INSERT INTO book_category (`book_id`, `category_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in cover_designer:
            cursor.execute(
                "INSERT INTO book_designer (`book_id`, `designer_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in language:
            cursor.execute(
                "INSERT INTO book_language (`book_id`, `language_id`) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in translator:
            cursor.execute(
                "INSERT INTO book_translator (book_id, translator_id) VALUES({}, {});".format(a, i))
            connection.commit()
        for i in resource:
            cursor.execute(
                "INSERT INTO resources_book (`book_id`, `resource_id`) VALUES({}, {});".format(a, i))
            connection.commit()

    @staticmethod
    def search(name: str = "", author_name: str = "", publisher_name: str = "", category_name: str = "", language_name: str = "", designer_name: str = "", translator_name: str = "", resource_name: str = ""):
        publishers = PublisherDataAdapter.search(
            publisher_name) if publisher_name != "" else PublisherDataAdapter.search("")
        publisher_id = [i.id for i in publishers if i != None]
        publishers = str(tuple(publisher_id)).replace(",)", ")")

        authors = AuthorDataAdapter.search(
            author_name) if author_name != "" else AuthorDataAdapter.search("")
        author_id = [i.id for i in authors if i != None]
        authors = str(tuple(author_id)).replace(",)", ")")

        categories = CategoryDataAdapter.search(
            category_name) if category_name != "" else CategoryDataAdapter.search("")
        category_id = [i.id for i in categories if i != None]
        categories = str(tuple(category_id)).replace(",)", ")")

        languages = LanguageDataAdapter.search(
            language_name) if language_name != "" else LanguageDataAdapter.search("")
        language_id = [i.id for i in languages if i != None]
        languages = str(tuple(language_id)).replace(",)", ")")

        designers = DesignerDataAdapter.search(
            designer_name) if designer_name != "" else DesignerDataAdapter.search("")
        designer_id = [i.id for i in designers if i != None]
        designers = str(tuple(designer_id)).replace(",)", ")")

        translators = TranslatorDataAdapter.search(
            translator_name) if translator_name != "" else TranslatorDataAdapter.search("")
        translator_id = [i.id for i in translators if i != None]
        translators = str(tuple(translator_id)).replace(",)", ")")

        resources = ResourcesDataAdapter.search(
            resource_name) if resource_name != "" else ResourcesDataAdapter.search("")
        resources_id = [i.id for i in resources if i != None]
        resources = str(tuple(resources_id)).replace(",)", ")")

        # print(publishers, authors, categories, languages,
        #       designers, translators, resources)

        s = cursor.execute("""SELECT books.id,books.title,books.product_code,books.age_group
                        ,books.publisher_id,books.release_date,books.price,author_id,category_id
                        ,designer_id,language_id,translator_id,resource_id  from books  
                         LEFT JOIN publishers on books.publisher_id = publishers.id  
                         LEFT JOIN book_author on books.id = book_author.book_id 
                         LEFT JOIN book_category on books.id = book_category.book_id 
                         LEFT JOIN book_language on books.id = book_language.book_id
                         LEFT JOIN book_designer on books.id = book_designer.book_id
                         LEFT JOIN book_translator on books.id = book_translator.book_id
                         LEFT JOIN resources_book on books.id = resources_book.book_id
                         
                         where (books.title like '%{}%') and (author_id in {}) and (publisher_id in {}) 
                         and (category_id in {}) and (designer_id in {}) and (language_id in {}) and 
                         (translator_id in {})  and (resource_id in {}) 
                         """.format(name, authors, publishers, categories, designers,
                                    languages, translators, resources))
        # print(list(s))
        table = list(s)

        categories = CategoryDataAdapter.get_all()
        authors = AuthorDataAdapter.get_all()
        publishers = PublisherDataAdapter.get_all()
        languages = LanguageDataAdapter.get_all()
        cover_designers = DesignerDataAdapter.get_all()
        translators = TranslatorDataAdapter.get_all()
        resources = ResourcesDataAdapter.get_all()

        books = []
        for row in table:
            book_id = row[0]
            title = row[1]
            product_code = row[2]
            age_group = row[3]
            publisher = publishers[publishers.index(row[4])]
            release_date = datetime.date.fromisoformat(row[5])
            price = row[6]

            # book_categories = [categories[categories.index(cat)] for cat in [
            #     cat_row[7] for cat_row in table if cat_row[0] == book_id] if cat is not None and not cat in book_categories]
            book_categories = []

            for cat_row in table:

                if cat_row[0] == book_id and cat_row[8] is not None and cat_row[8] not in book_categories:

                    book_categories.append(
                        categories[categories.index(cat_row[8])])

        #     book_authors = [authors[authors.index(author)] for author in [
        #         author_row[8] for author_row in table if author_row[0] == book_id] if author is not None]
            book_authors = []

            for auth_row in table:

                if auth_row[0] == book_id and auth_row[7] is not None and auth_row[7] not in book_authors:

                    book_authors.append(authors[authors.index(auth_row[7])])

        #     book_languages = [languages[languages.index(language)] for language in [
        #         language_row[9] for language_row in table if language_row[0] == book_id] if language is not None]
            book_languages = []
            for lang_row in table:
                if lang_row[0] == book_id and lang_row[10] is not None and lang_row[10] not in book_languages:
                    book_languages.append(
                        languages[languages.index(lang_row[10])])

        #     book_designers = [cover_designers[cover_designers.index(designer)] for designer in [
        #         designer_row[10] for designer_row in table if designer_row[0] == book_id] if designer is not None]
            book_designers = []
            for des_row in table:
                if des_row[0] == book_id and des_row[9] is not None and des_row[9] not in book_designers:
                    book_designers.append(
                        cover_designers[cover_designers.index(des_row[9])])

        #     book_translators = [translators[translators.index(translator)] for translator in [
        #         translator_row[11] for translator_row in table if translator_row[0] == book_id] if translator is not None]
            book_translators = []
            for tran_row in table:
                if tran_row[0] == book_id and tran_row[11] is not None and tran_row[11] not in book_translators:
                    book_translators.append(
                        translators[translators.index(tran_row[11])])

        #     book_resources = [resources[resources.index(resource)] for resource in [
        #         resources_row[12] for resources_row in table if resources_row[0] == book_id] if resource is not None]
            book_resources = []
            for res_row in table:
                if res_row[0] == book_id and res_row[12] is not None and res_row[12] not in book_resources:
                    book_resources.append(
                        resources[resources.index(res_row[12])])

            books.append(model.Book(
                id=book_id,
                title=title,
                product_code=product_code,
                categories=book_categories,
                age_group=age_group,
                authors=book_authors,
                publisher=publisher,
                release_date=release_date,
                price=price,
                languages=book_languages,
                cover_designers=book_designers,
                translators=book_translators,
                resources=book_resources))
        newbooks = []
        for i in books:
            status = True
            for j in newbooks:
                if j.id == i.id:
                    status = False
            if status:
                newbooks.append(i)
        return newbooks
