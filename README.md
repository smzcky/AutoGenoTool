�������ƣ���������С����

�汾��1.0

���ܣ����� App_Com.c��CanSys.if.h��CanSys_SigAccess.c��CanSys_SigAccess.h�ļ�����Ҫ�ֹ����õĸ�ʽ�ظ���
      �ӿڼ�ö������

�÷���
      ���룺
      ���д˳�����Ҫ��װPython3�����ϰ汾���˳�����Ҫһ��ԭʼ�ļ����ļ���ʽ���⣩��Ϊ�������룬
      �ļ�������Ҫ�ֶ�Ϊ��������
      DATASEG_Tx_Message����Ϊ��һ�Σ�
      #define COM_TXIPDUICM_VehSt    (0U)        ������������Com.cfg.h�еķ��ͱ��ģ�
      DATASEG_Tx_Signal����Ϊ�ڶ��Σ�
      /*ICM_VehSt S4_ICM_geno*/
      #define COM_TXSIGAvgFuelConsumption (0U)   ������������Com.cfg.h�еķ����źţ�
      DATASEG_Rx_Message����Ϊ�����Σ�	
      #define COM_RXIPDUSRS_CrashInfo    (0U)    ������������Com.cfg.h�еĽ��ձ��ģ�
      DATASEG_Rx_Signal����Ϊ���ĶΣ�
      /*SRS_CrashInfo S4_ICM_geno*/
      #define COM_RXSIGSRS_StatusCheckSum   (0U) ������������Com.cfg.h�еĽ����źţ�

      ����ɼ�ʵ���ļ�����Com.cfg.h�ļ��н����ݸ��������������ϸ�ʽ���м��ɡ�
      ִ�У�
      ���д˳�����start.vbs���ɣ�����۲�cmd���Գ��򣬿ɵ��support.bat���г���

��֪ȱ�ݣ����ɵ�CanSys_SigAccess�ļ��нӿڲ��������޷�ȷ����uint8��uint16��uint32����Ϊ16��32λ���٣��õĲ�������
ȫΪuint8��������Ҫ�ҳ�16��32λ�����Ľӿڽ����޸ġ�