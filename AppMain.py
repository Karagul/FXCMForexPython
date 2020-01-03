from forexconnect import fxcorepy, ForexConnect

user_id = ""
password = ""
def session_status_changed(session: fxcorepy.O2GSession,
                           status: fxcorepy.AO2GSessionStatus.O2GSessionStatus):
    print("Trading session status: " + str(status))


def main():
    with ForexConnect() as fx:
        try:
            #fxcorporate.com/Hosts.jsp
            #http://www.fxcorporate.com/Hosts.jsp
            fx.login(user_id, password, "fxcorporate.com/Hosts.jsp",
                     "demo", session_status_callback=session_status_changed)
            print("Exception: " + str(e))

        # TBD: your ForexConnect API logic here.

        except Exception as e:
            print("Exception: " + str(e))


        try:
            fx.logout()
        except Exception as e:
            print("Exception: " + str(e))


if __name__ == "__main__":
    main()
