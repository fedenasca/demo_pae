#-------------------------------------------------------------------------------#
#	PASO 2.1: 	SELECCION Y CATEGORIZACION DE VARIABLES (F)	        #
#-------------------------------------------------------------------------------#

#################################################################################
#	RAW VARIABLES (F)                                                       #
#################################################################################

# Variable selection from Raw Dataset

raw_variables_F = [
    #MES - PARTICION                
                "month_dt"
    #CLIENTE - ID
                ,"subscription_id"
                ,"msisdn_id"
    #CLIENTE - VALOR
        #app "mi movistar"
                ,"segmento_cluster_app_novum"  #VS_F2
                ,"perfil_digital_app_novum" #VS_F2
        #equipo        
#               ,"marca"
#                ,"modelo"
                ,"tecnologia_equipo" #VS_F2
                ,"so" #VS_F2
                ,"red"  #VS_F2
        #historico
                ,"meses_cater_qt" #VS_F2
               ,"ant_meses" #VS_F2
        #perfil
                ,"grupo_hu" #VS_F2
            #indicador - kpi
                ,"score_migra" #VS_F2
                ,"rango_migra" #VS_F2
                ,"percentil_promedio" #VS_F2
    #EXPERIENCIA USUARIO
        #trafico de datos
                ,"zona_performance"  #VS_F2 
            #derivado
                ,"offloading" #VS_F2
            #indicador -kpi
                ,"indicador_thp" #VS_F2
                ,"cei_porcentaje_score_60" #VS_F2
                ,"cei_qoe_web" #VS_F2
                ,"cei_qoe_streaming"                 #VS_F2
                ,"cei_qoe_mensajeria_inst"  #VS_F2
                ,"cei_qoe_voip"  #VS_F2
                ,"cei_qoe_archivos"  #VS_F2
                ,"cei_qoe_sms"  #VS_F2
                ,"cei_qoe_voz"  #VS_F2
                ,"cei_indice_experiencia_datos"  #VS_F2
                ,"cei_indice_experiencia_total"  #VS_F2
        #trafico de voz
#                ,"q_dc"
    #FLAG
        #cliente - valor
            #equipo
#                ,"sim_lte"
#                ,"f_eq_interno"
#                ,"fl_cater"
#                ,"fl_csim"
#                ,"fl_simlock"
#                ,"fl_empleados"
            #perfil
#                ,"fl_lista_negra"
#                ,"fl_no_llame"
#                ,"fl_casim_neg"
                ,"fl_navegador"  #VS_F2
                ,"fl_migrable"  #VS_F2
                ,"fl_sitio_4g"  #VS_F2
        #interaccion con la compania 
            #app "mi movistar"
                ,"fl_app_novum"  #VS_F2
            #campania
#                ,"fl_filtro_campana"
            #campania - migra
#                ,"fl_camp_migra"
            #campania - pirs
                ,"fl_camp_pirs"  #No lo tenemos para el mes de prediccion, pero si puede ir de filtro 
            #campania - televenta
#                ,"fl_televentas_30"
            #reclamo
#                ,"fl_visita_cec"
        #operaciones
            #caduca
                ,"fl_pack_caduca"  #VS_F2
            #migra pirs
                ,"fl_migra_pir_neutra" #lo dejo a proposito, por completitud
                ,"fl_migra_pir_positiva" #lo dejo a proposito, por completitud
                ,"fl_migra_pir_negativa" #lo dejo a proposito, por completitud
                ,"fl_migra_pir_sym" #lo dejo a proposito, por completitud
            #movimiento
#                ,"fl_alta"
#                ,"fl_migrapos"
            #pack individual
                ,"fl3_bono"  #VS_F2
            #packs combinados
                ,"fl1_pirs" #lo dejo a proposito, por completitud
                ,"fl1_ultra" #lo dejo a proposito, por completitud
                ,"fl1_super" ##lo dejo a proposito, por completitud
                ,"fl1_plus" ##lo dejo a proposito, por completitud
                ,"fl1_extra" ##lo dejo a proposito, por completitud
                ,"fl1_semana" ##lo dejo a proposito, por completitud
                ,"fl1_mes" ##lo dejo a proposito, por completitud
                ,"fl10_solo_semana" ##lo dejo a proposito, por completitud
                ,"fl10_solo_mes" ##lo dejo a proposito, por completitud
                ,"fl10_solo_mesysemana" #lo dejo a proposito, por completitud
            #recarga
                ,"fl2_recarga" #VS_F2
    #GEOLOCALIZACION
#                ,"region_ddn"
#                ,"subregion_ddn"
#                ,"region_vive_red" -------------------------NULLLLLLLLLLLLLLLLLL
                ,"provincia_vive_red"   #VS_F2
#                ,"region_trabaja_red"  --------- No se considera porque corta por NULLLLLLLLLLLLLLLLLLLLLL
#                ,"provincia_trabaja_red" No se considera porque corta por NULLLLLLLLLLLLLLLLLLLLLLL
#                ,"region_comercial" --------- No se considera porque corta por NULLLLLLLLLLLLLLLLLLLLLLLL
#                ,"subregion_comercial" --------- No se considera porque corta por NULLLLLLLLLLLLLLLLLLL
    #INTERACCION CON LA COMPAniIA
#                ,"qt_tkt_atencion_gral"
#                ,"qt_tkt_contingencia"
#                ,"qt_tkt_eq_sim"
#                ,"qt_tkt_fidelizacion"
#                ,"qt_tkt_red"
#                ,"qt_tkt_retencion"
        #app "mi movistar"
                ,"version_app_novum"   #VS_F2
                ,"interface_app_novum" #VS_F2
#                ,"first_login_app_novum"
        #campania
                ,"rtd" #VS_F2
#                ,"qt_camp_inc_recargas"
#                ,"qt_camp_informacion"
            #packs combinados
#                ,"q_recom" --------------------No se considera por desfasaje
#                ,"q_recom_ultra"
#                ,"q_recom_super" ---------------No se considera por desfasaje
#                ,"q_recom_plus" ----------------No se considera por desfasaje
#                ,"q_recom_extra" ---------------No se considera por desfasaje
#                ,"q_recom_semana"
#                ,"q_recom_mes"
        #reclamo
#                ,"qt_tkt_reclamos_sugerencias"
#                ,"qt_tkt_serv_tecnico"
#                ,"call_611_1l_tot_qt"
#                ,"call_611_1l_com_qt"
#                ,"call_611_1l_rell_qt"
#                ,"call_611_1l_tec_qt"
#                ,"call_611_2l_ret_qt"
    #OPERACIONES
        #bonus
            #multiplicate
                ,"multi_qt"  #VS_F2 
                ,"amt_multi"  #VS_F2
                ,"multi_x2_qt" #VS_F2
                ,"multi_x3_qt" #VS_F2
                ,"multi_x4_qt" #lo dejo a proposito, por completitud
                ,"multi_x5_qt" #VS_F2
                ,"multi_x6_qt" #VS_F2
                ,"multi_x7_qt" #VS_F2
            #packs combinados
                ,"amt_pack_pirs" ##lo dejo a proposito, por completitud
                ,"qt_pack_pirs" ##lo dejo a proposito, por completitud
                ,"amt_pack_semana" ##lo dejo a proposito, por completitud
                ,"qt_pack_semana" ##lo dejo a proposito, por completitud
                ,"amt_pack_mes" ##lo dejo a proposito, por completitud
                ,"qt_pack_mes" ##lo dejo a proposito, por completitud
                ,"amt_pack_semana_ultra"    #lo dejo a proposito, por completitud
                ,"qt_pack_semana_ultra" #lo dejo a proposito, por completitud
                ,"amt_pack_semana_extra" ##lo dejo a proposito, por completitud
                ,"qt_pack_semana_extra" ##lo dejo a proposito, por completitud
                ,"amt_pack_semana_plus" ##lo dejo a proposito, por completitud
                ,"qt_pack_semana_plus" ##lo dejo a proposito, por completitud
                ,"amt_pack_semana_super" ##lo dejo a proposito, por completitud
                ,"qt_pack_semana_super" ##lo dejo a proposito, por completitud
                ,"packu_mes" ##lo dejo a proposito, por completitud
            #packs individuales
                ,"amt_bono"  #VS_F2
                ,"qt_bono"  #VS_F2
                ,"amt_bono_datos"  #VS_F2
                ,"qt_bono_datos"  #VS_F2
                ,"amt_bono_combinados"  #VS_F2
                ,"qt_bono_combinados"  #VS_F2
#                ,"amt_bono_ldi"
#                ,"qt_bono_ldi"
#                ,"amt_bono_minutos"
#                ,"qt_bono_minutos"
#                ,"amt_bono_sms"
#                ,"qt_bono_sms"
        #recarga
                ,"arpu_negocio_promedio"  #VS_F2
                ,"qt_internet_por_dia"  #VS_F2
                ,"amt_recargas"  #VS_F2
                ,"qt_recargas"  #VS_F2
                ,"amt_recarga"  #VS_F2
                ,"qt_recarga"  #VS_F2
            #primera recarga
#                ,"amt_1recarga"
            #tipo recarga
                ,"amt_recarga_promocional"  #VS_F2
                ,"qt_recarga_promocional"  #VS_F2
                ,"amt_recarga_sos"  #VS_F2
                ,"qt_recarga_sos"  #VS_F2
                ,"amt_recarga_electronica"  #VS_F2
                ,"qt_recarga_electronica"  #VS_F2
#                ,"amt_recarga_rebatem"
#                ,"qt_recarga_rebatem"
                ,"amt_recarga_saldoexp"   #VS_F2
                ,"qt_recarga_saldoexp" #lo dejo a proposito, por completitud
#                ,"amt_recarga_pinmovistar"
#                ,"qt_recarga_pinmovistar"
                ,"amt_recarga_otros" #lo dejo a proposito, por completitud
                ,"qt_recarga_otros" #VS_F2
    #TARGET
        #pack individual
                ,"t3_bono"
        #packs combinados
                ,"t_pack"
                ,"t1_pirs"
                ,"t1_ultra"
                ,"t1_super"
                ,"t1_plus"
                ,"t1_extra"
                ,"t1_semana"
                ,"t1_mes"
                ,"t10_solo_semana"
                ,"t10_solo_mes"
                ,"t10_solo_mesysemana"
        #recarga
                ,"t2_recarga"
    #TRAFICO
                ,"cei_dias_con_trafico"  #VS_F2
        #trafico datos
                ,"mb_2g_qt"  #VS_F2
                ,"mb_3g_qt"  #VS_F2
                ,"mb_4g_qt"  #VS_F2
                ,"duration_2g"  #VS_F2
                ,"duration_3g"  #VS_F2
                ,"duration_4g"  #VS_F2
                ,"cei_trafico_web"  #VS_F2
                ,"cei_trafico_streaming"  #VS_F2
                ,"cei_trafico_mensajeria_inst"  #VS_F2
                ,"cei_trafico_voip"  #VS_F2
                ,"cei_trafico_archivos"  #VS_F2
            #competencia
#                ,"cablevision_fiber"
#                ,"claro"
#                ,"personal"
#                ,"nextel"
            #derivada
                ,"tiempo_4g"  #VS_F2
                ,"mb_total_qt"  #VS_F2
                ,"duration_total"  #VS_F2
            #funapp
                ,"trafico_mb_twitter"  #VS_F2
                ,"duracion_twitter"  #VS_F2
                ,"q_dias_twitter"  #VS_F2
                ,"trafico_mb_facebook"  #VS_F2
                ,"duracion_facebook"  #VS_F2
                ,"q_dias_facebook"  #VS_F2
#                ,"trafico_mb_facebook_voz"
#                ,"duracion_facebook_voz"
#                ,"q_dias_facebook_voz"
                ,"trafico_mb_youtube"   #VS_F2 
                ,"duracion_youtube"   #VS_F2
                ,"q_dias_youtube"  #VS_F2
#                ,"trafico_mb_waze"
#                ,"duracion_waze"
#                ,"q_dias_waze"
                ,"trafico_mb_whatsapp_voz"  #VS_F2
                ,"duracion_whatsapp_voz"   #VS_F2 
                ,"q_dias_whatsapp_voz"   #VS_F2
                ,"trafico_mb_whatsapp_chat"  #VS_F2
                ,"duracion_whatsapp_chat"  #VS_F2
                ,"q_dias_whatsapp_chat"  #VS_F2
                ,"trafico_mb_instagram"   #VS_F2
                ,"duracion_instagram"  #VS_F2
                ,"q_dias_instagram"  #VS_F2
                ,"trafico_mb_netflix"  #VS_F2
                ,"duracion_netflix"  #VS_F2
                ,"q_dias_netflix"  #VS_F2
                ,"trafico_mb_spotify"  #VS_F2
                ,"duracion_spotify"  #VS_F2
                ,"q_dias_spotify"  #VS_F2
                ,"trafico_mb_snapchat" #VS_F2
                ,"duracion_snapchat"  #VS_F2
                ,"q_dias_snapchat"  #VS_F2
#                ,"trafico_mb_snapchat_voz"
#                ,"duracion_snapchat_voz"
#                ,"q_dias_snapchat_voz"
                ,"trafico_mb_google_maps"  #VS_F2
                ,"duracion_google_maps"  #VS_F2
                ,"q_dias_google_maps"   #VS_F2
        #trafico sms
                ,"cei_trafico_sms"  #VS_F2
        #trafico voz
                ,"duration_2gv"  #VS_F2
                ,"qllamadas_2gv"  #VS_F2
                ,"duration_3gv"  #VS_F2
                ,"qllamadas_3gv"  #VS_F2
                ,"minutos_totalesv_sal"  #VS_F2
                ,"llamadas_totalesv_sal"  #VS_F2
                ,"minutos_totalesv_ent"  #VS_F2
                ,"llamadas_totalesv_ent"  #VS_F2
#                ,"minutos_tasa_sal"
#                ,"minutos_tasa_ent"
                ,"cei_trafico_voz"  #VS_F2
            #competencia
                ,"minutos_onnet_sal"  #VS_F2
                ,"minutos_claro_sal"  #VS_F2
                ,"minutos_personal_sal" #lo dejo a proposito, por completitud
                ,"minutos_offnet_sal"  #VS_F2
                ,"minutos_onnet_ent"  #VS_F2
                ,"minutos_claro_ent" #VS_F2
                ,"minutos_personal_ent"  #VS_F2
                ,"minutos_offnet_ent"  #VS_F2
#                ,"cvs_q_llam_out"
#                ,"cvs_max_seg_dur_out"
#                ,"clr_q_llam_out"
#                ,"clr_max_seg_dur_out"
#                ,"teco_q_llam_out"
#                ,"teco_max_seg_dur_out"
#                ,"cvs_q_llam_in"
#                ,"cvs_max_seg_dur_in"
#                ,"clr_q_llam_in"
#                ,"clr_max_seg_dur_in"
#                ,"teco_q_llam_in"
#                ,"teco_max_seg_dur_in"
                ]

# Data type raw variables
raw_variables_int_F = [
#"month_dt" Se consideran todas las variables int, menos month_dt y msisdn_id. Funcion falla con date
#,"msisdn_id"
"meses_cater_qt"
,"ant_meses"
,"percentil_promedio"
,"cei_qoe_web"
,"cei_qoe_streaming"
,"cei_qoe_mensajeria_inst"
,"cei_qoe_voip"
,"cei_qoe_archivos"
,"cei_qoe_sms"
,"cei_qoe_voz"
,"cei_indice_experiencia_datos"
,"cei_indice_experiencia_total"
,"fl_navegador"
,"fl_migrable"
,"fl_sitio_4g"
,"fl_app_novum"
,"fl_camp_pirs"
,"fl_pack_caduca"
,"fl_migra_pir_neutra"
,"fl_migra_pir_positiva"
,"fl_migra_pir_negativa"
,"fl_migra_pir_sym"
,"fl3_bono"
,"fl1_pirs"
,"fl1_ultra"
,"fl1_super"
,"fl1_plus"
,"fl1_extra"
,"fl1_semana"
,"fl1_mes"
,"fl10_solo_semana"
,"fl10_solo_mes"
,"fl10_solo_mesysemana"
,"fl2_recarga"
,"qt_pack_pirs"
,"qt_pack_semana"
,"qt_pack_mes"
,"qt_pack_semana_ultra"
,"qt_pack_semana_extra"
,"qt_pack_semana_plus"
,"qt_pack_semana_super"
,"qt_bono"
,"qt_bono_datos"
,"qt_bono_combinados"
,"qt_recargas"
,"qt_recarga"
,"qt_recarga_promocional"
,"qt_recarga_sos"
,"qt_recarga_electronica"
,"qt_recarga_saldoexp"
,"qt_recarga_otros"
,"t3_bono"
,"t1_pirs"
,"t1_ultra"
,"t1_super"
,"t1_plus"
,"t1_extra"
,"t1_semana"
,"t1_mes"
,"t10_solo_semana"
,"t10_solo_mes"
,"t10_solo_mesysemana"
,"t2_recarga"
,"cei_dias_con_trafico"
,"cei_trafico_web"
,"cei_trafico_streaming"
,"cei_trafico_mensajeria_inst"
,"cei_trafico_voip"
,"cei_trafico_archivos"
,"q_dias_twitter"
,"q_dias_facebook"
,"q_dias_youtube"
,"q_dias_whatsapp_voz"
,"q_dias_whatsapp_chat"
,"q_dias_instagram"
,"q_dias_netflix"
,"q_dias_spotify"
,"q_dias_snapchat"
,"q_dias_google_maps"
,"cei_trafico_sms"
,"qllamadas_2gv"
,"qllamadas_3gv"
,"cei_trafico_voz"
,"multi_qt"
,"multi_x2_qt"
,"multi_x3_qt"
,"multi_x4_qt"
,"multi_x5_qt"
,"multi_x6_qt"
,"multi_x7_qt"
,"qt_internet_por_dia"

]

raw_variables_float_F = [
"subscription_id"
,"score_migra"
,"offloading"
,"indicador_thp"
,"cei_porcentaje_score_60"
,"rtd"
,"arpu_negocio_promedio"
,"mb_2g_qt"
,"mb_3g_qt"
,"mb_4g_qt"
,"duration_2g"
,"duration_3g"
,"duration_4g"
,"mb_total_qt"
,"duration_total"
,"amt_pack_pirs"
,"amt_pack_semana"
,"amt_pack_mes"
,"amt_pack_semana_ultra"
,"amt_pack_semana_extra"
,"amt_pack_semana_plus"
,"amt_pack_semana_super"
,"amt_multi"
,"amt_bono"
,"amt_bono_datos"
,"amt_bono_combinados"
,"amt_recargas"
,"amt_recarga"
,"amt_recarga_promocional"
,"amt_recarga_sos"
,"amt_recarga_electronica"
,"amt_recarga_saldoexp"
,"amt_recarga_otros"
,"tiempo_4g"
,"trafico_mb_twitter"
,"duracion_twitter"
,"trafico_mb_facebook"
,"duracion_facebook"
,"trafico_mb_youtube"
,"duracion_youtube"
,"trafico_mb_whatsapp_voz"
,"duracion_whatsapp_voz"
,"trafico_mb_whatsapp_chat"
,"duracion_whatsapp_chat"
,"trafico_mb_instagram"
,"duracion_instagram"
,"trafico_mb_netflix"
,"duracion_netflix"
,"trafico_mb_spotify"
,"duracion_spotify"
,"trafico_mb_snapchat"
,"duracion_snapchat"
,"trafico_mb_google_maps"
,"duracion_google_maps"
,"duration_2gv"
,"duration_3gv"
,"minutos_totalesv_sal"
,"llamadas_totalesv_sal"
,"minutos_totalesv_ent"
,"llamadas_totalesv_ent"
,"minutos_onnet_sal"
,"minutos_claro_sal"
,"minutos_personal_sal"
,"minutos_offnet_sal"
,"minutos_onnet_ent"
,"minutos_claro_ent"
,"minutos_personal_ent"
,"minutos_offnet_ent"

]

raw_variables_string_F =[
"segmento_cluster_app_novum"
,"perfil_digital_app_novum"
,"tecnologia_equipo"
,"so"
,"red"
,"grupo_hu"
,"rango_migra"
,"zona_performance"
,"provincia_vive_red"
,"version_app_novum"
,"interface_app_novum"
,"packu_mes"
,"t_pack"

]