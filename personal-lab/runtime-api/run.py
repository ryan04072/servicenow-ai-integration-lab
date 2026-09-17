from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
import uvicorn
from app import app
if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)
