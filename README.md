工具名称：代码生成小工具

版本：1.0

功能：生成 App_Com.c、CanSys.if.h、CanSys_SigAccess.c、CanSys_SigAccess.h文件中需要手工配置的格式重复的
      接口及枚举类型

用法：
      输入：
      运行此程序需要安装Python3及以上版本，此程序需要一个原始文件（文件格式随意）作为数据输入，
      文件数据需要分段为（例）：
      DATASEG_Tx_Message（此为第一段）
      #define COM_TXIPDUICM_VehSt    (0U)        （工具生成在Com.cfg.h中的发送报文）
      DATASEG_Tx_Signal（此为第二段）
      /*ICM_VehSt S4_ICM_geno*/
      #define COM_TXSIGAvgFuelConsumption (0U)   （工具生成在Com.cfg.h中的发送信号）
      DATASEG_Rx_Message（此为第三段）	
      #define COM_RXIPDUSRS_CrashInfo    (0U)    （工具生成在Com.cfg.h中的接收报文）
      DATASEG_Rx_Signal（此为第四段）
      /*SRS_CrashInfo S4_ICM_geno*/
      #define COM_RXSIGSRS_StatusCheckSum   (0U) （工具生成在Com.cfg.h中的接收信号）

      具体可见实例文件，在Com.cfg.h文件中将数据复制下来按照以上格式排列即可。
      执行：
      运行此程序点击start.vbs即可，如需观察cmd调试程序，可点击support.bat运行程序。

已知缺陷：生成的CanSys_SigAccess文件中接口参数类型无法确定是uint8、uint16、uint32，因为16和32位较少，用的参数类型
全为uint8，所以需要找出16和32位参数的接口进行修改。