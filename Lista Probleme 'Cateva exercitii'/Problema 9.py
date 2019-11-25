import datetime
def how_older_have(nr_of_secound_total):
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    nr_of_secound_in_normal_year=31536000
    nr_of_secound_in_ennormal_year=31622400
    nr_of_secound_in_day=86400
    nr_of_secound_in_month = [31 * 24 * 60 * 60, 28 * 24 * 60 * 60, 31 * 24 * 60 * 60, 30 * 24 * 60 * 60,
                              31 * 24 * 60 * 60, 30 * 24 * 60 * 60, 31 * 24 * 60 * 60, 31 * 24 * 60 * 60,
                              30 * 24 * 60 * 60, 31 * 24 * 60 * 60, 30 * 24 * 60 * 60, 31 * 24 * 60 * 60]
    the_time = [int(now.strftime('%Y')), int(now.strftime('%m')), int(now.strftime("%d")), int(now.strftime('%H')),
                int(now.strftime('%M')), int(now.strftime('%S'))]
    if the_time[0]%4 == 0:
        nr_of_secound_in_yearO=nr_of_secound_in_ennormal_year
    else:
        nr_of_secound_in_yearO =nr_of_secound_in_normal_year
    while nr_of_secound_total > nr_of_secound_in_yearO :
        nr_of_secound_total-=nr_of_secound_in_yearO
        the_time[0] -=1
        if the_time[0] % 4 == 0  and (the_time[0]%100 !=0 or the_time[0] % 400 == 0):
            nr_of_secound_in_yearO = nr_of_secound_in_ennormal_year
        else:
            nr_of_secound_in_yearO = nr_of_secound_in_normal_year
    print(nr_of_secound_total)
    while nr_of_secound_total > nr_of_secound_in_month[the_time[1]-1]:
        nr_of_secound_total -= int(nr_of_secound_in_month[the_time[1]-1])
        the_time[1] -= 1
        if the_time[1] == 0 :
            the_time[1] = 12
            the_time[0] -= 1
    while nr_of_secound_total > nr_of_secound_in_day :
        nr_of_secound_total -= nr_of_secound_in_day
        the_time[2] -= 1
        if the_time[2] == 0:
            if the_time[1] != 1:
                the_time[1] -= 1
            else:
                the_time[1] = 12
                the_time[0] -= 1
            the_time[2] = int(nr_of_secound_in_month[the_time[1]]) % (24 * 60 * 60)
    print('vârsta lui Dorel')
    month = int(now.strftime('%m')) - the_time[1]
    if month < 1:
        month = 12 - month
    day = int(now.strftime('%d')) - the_time[2]
    if day < 1:
        day = int(nr_of_secound_in_month[the_time[1]]) % (24 * 60 * 60) - day
    print('are', int(now.strftime('%Y')) - the_time[0], 'an si',month, 'luna si', day, 'de zila')
    print('Dora sa nascut in data')
    print(the_time)


nr_of_secound_total=int(input('nr de seconde ='))
if __name__ == '__main__':
    how_older_have(nr_of_secound_total)