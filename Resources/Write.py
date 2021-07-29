class Write:
    @staticmethod
    def results():
        print("writing........")
        f = open(r"C:\Users\HP 1040 G2\PycharmProjects\log_file.txt")
        line = f.readline()
        detail = ['', '', '', '', '']
        summary = ['', '', '', '', '']
        task_counter = 0
        is_detail = True
        while line:
            print(line)
            if 'Ran 5 tests' in line:
                line = f.readline()
                continue

            if 'SUMMARY' in line:
                is_detail = False
                line = f.readline()
                continue

            if 'Beginning TASK' in line:
                task_counter += 1
                is_detail = True
                line = f.readline()
                continue

            if is_detail:
                detail[task_counter] = detail[task_counter] + line + '<br>'
            else:
                summary[task_counter] = summary[task_counter] + line + '<br>'

            line = f.readline()

        f.close()

        GEN_HTML = "log.html"

        f = open(GEN_HTML, 'w')
        message = f"""
        <html>
        <head><title>Assignment 1</title></head>
        <body>

        <table border='1'>
            <tr>
            <th>Task</th>
            <th>Summary</th>
            <th>Details</th>
        </tr>
        <tr>
            <td>1</td>
            <td>{summary[0]}</td>
            <td>{detail[0]}</td>
        </tr>
        <tr>
            <td>2</td>
            <td>{summary[1]}</td>
            <td>{detail[1]}</td>
        </tr>
        <tr>
            <td>3</td>
            <td>{summary[2]}</td>
            <td>{detail[2]}</td>
        </tr>
        <tr>
            <td>4</td>
            <td>{summary[3]}</td>
            <td>{detail[3]}</td>
        </tr>
        <tr>
            <td>5</td>
            <td>{summary[4]}</td>
            <td>{detail[4]}</td>
        </tr>
    </body>
    </html>"""

        f.write(message)
        f.close()
