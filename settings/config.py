""" Типы"""

from typing import Self, Optional, List, Dict

############################################
"""Прочие необходимые библиотеки"""
import shutil
import random
import traceback
import configparser
from threading import Thread
from ast import literal_eval
import platform
import csv
import sys
import time
import os
import re
import json

########################################### 
import datetime

'''
Bot development
'''
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router, types, F
from aiogram.types import Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.filters.callback_data import CallbackData
from aiogram.enums import ParseMode
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile


DEBUG = True

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import aiohttp
import redis
import xml.etree.ElementTree as ET


config = configparser.ConfigParser()
config.read(r'settings/settings.ini')  # читаем конфиг


CB_URL = "https://www.cbr.ru/scripts/XML_daily.asp"
UPDATE_INTERVAL = 24 * 60 * 60  # 24 hours in seconds

# Redis settings
REDIS_HOST = config['redis']['host']
REDIS_PORT = int(config['redis']['port'])
REDIS_DB = int(config['redis']['db'])

def config_update():
    with open(r'settings/settings.ini', 'w') as f:
        config.write(f)
    config.read(r'settings/settings.ini')

import logging
logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"
)
