import librosa
import numpy as np

def detect_highlights(video_path, whisper_segments, top_n=5):
    """
    video_path: 영상 파일 경로
    whisper_segments: Whisper가 반환한 [{start, end, text}, ...] 리스트
    top_n: 최종적으로 추출할 하이라이트 개수
    """
    
    # 1. 오디오 로드 및 데시벨 분석
    y, sr = librosa.load(video_path, sr=None)
    # RMS(Root Mean Square) 에너지 계산
    rms = librosa.feature.rms(y=y)[0]
    times = librosa.frames_to_time(range(len(rms)), sr=sr)
    
    # 감탄사 리스트 (프로젝트 성격에 따라 추가 가능)
    reaction_keywords = ["와", "대박", "헐", "오", "우와", "레전드", "나이스", "대단"]

    highlight_candidates = []

    for segment in whisper_segments:
        start = segment['start']
        end = segment['end']
        text = segment['text']

        # 해당 구간의 평균 데시벨 계산
        idx = np.where((times >= start) & (times <= end))
        avg_rms = np.mean(rms[idx]) if len(idx[0]) > 0 else 0
        
        # 점수 산정 로직 (데시벨 기반)
        score = avg_rms * 100 
        
        # 2차 필터: 감탄사 포함 시 가산점 부여 (점수 2배!)
        is_reaction = any(word in text for word in reaction_keywords)
        if is_reaction:
            score *= 2.0
            
        highlight_candidates.append({
            'start': start,
            'end': end,
            'text': text,
            'score': score,
            'is_reaction': is_reaction
        })

    # 점수가 높은 순으로 정렬 후 상위 n개 반환
    highlight_candidates.sort(key=lambda x: x['score'], reverse=True)
    return highlight_candidates[:top_n]