/********** Kana Picking Project ***********/

DESCRIPTION OF DEVICES
    RBT = Melfa Robot (Server to PC 1[192.168.3.5 ::10006])
    PC 0 = PC sending the initial Kana data (Client to PC 1)
    PC 1 = PC receiving Kana data from PC 1 and transferring them to RBT (Server to PC 0[127.0.0.1 :: 1024] and Client to RBT [192.168.3.6])
    PLC [192.168.3.250]

SETTINGS OF DEVICES
    PLC:
        以下はCC-LINKの設定
            曲種別：マスタ局
            モード：リモートネットVer.2モード
            局番：０
            転送速度：10Mbps
            基本設定：パラメータ設定

            CC-LINK構成設定：局番０ーー＞汎用インテリジェントデバイス
            リンクリフレッシュ：
                RX: 
                    リンク側：128点数　先頭０
                    CPU側：リフレッシュ先＝指定デバイス、デバイス名＝X、点数＝128、先頭＝100、最終＝277 
                RY: 
                    リンク側：128点数　先頭０
                    CPU側：リフレッシュ先＝指定デバイス、デバイス名＝Y、点数＝128、先頭＝0、最終＝177 
                RWr: 
                    リンク側：32点数　先頭０
                    CPU側：リフレッシュ先＝指定デバイス、デバイス名＝D、点数＝32、先頭＝0、最終＝31
                RWw: 
                    リンク側：32点数　先頭０
                    CPU側：リフレッシュ先＝指定デバイス、デバイス名＝D、点数＝32、先頭＝1000、最終＝1031

        以下はイーサネットの設定
            IPアドレス：192.168.3.250
            相手機器接続構成設定：自局ーー＞MELSOFT接続ーー＞SLMP接続（現段階不要）
    

    ROBOT: 
        IO: (Inputs & Outputs of the PLC can act as an extension of the Robot's IOs through CC-LINK connection)
            Xs on PLC ==> From M_Out(6000)
            Yx on PLC ==> From M_In(6000)
            Wr on PLC ==> From M_Dout(6000)
            Ww on PLC ==> From M_Din(6000)
