import pygame, sys
from game_logic import Board
from ai_agent import ai_move

pygame.init()
SIZE = 4
TILE = 80
GAP = 10
FONT = pygame.font.SysFont("arial", 28, bold=True)

COLORS = {0:(180,180,180),2:(240,240,200),4:(250,230,180),8:(250,200,100),
          16:(250,170,80),32:(250,140,70),64:(250,100,50),128:(245, 245, 0),
          256:(240,220, 0),512:(240,200, 0),1024:(240,180, 0),2048:(255,160, 0)}

W = (TILE+GAP)*SIZE*2 + 100
H = (TILE+GAP)*SIZE + 100
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("2048 Human vs AI")

human = Board()
ai = Board()
clock = pygame.time.Clock()

def check_game_over(human, ai):
    if not human.can_move() and not ai.can_move():
        if human.score > ai.score: return "win"
        elif human.score < ai.score: return "lose"
        return "draw"
    return None

def end_screen(result):
    msg = {"win": "KAZANDIN! 🥳🔥","lose": "AI KAZANDI 🤖💔","draw": "BERABERE 😌"}[result]

    for fade in range(0, 255, 5):
        overlay = pygame.Surface((W, H))
        overlay.set_alpha(fade)
        overlay.fill((0,0,0))
        screen.blit(overlay, (0,0))

        text = FONT.render(msg, True, (255,255,255))
        screen.blit(text, text.get_rect(center=(W//2, H//2 - 20)))

        text2 = pygame.font.SysFont("arial", 22).render("Enter'a bas yeni oyun", True, (200,200,200))
        screen.blit(text2, text2.get_rect(center=(W//2, H//2 + 20)))

        pygame.display.update()
        pygame.time.delay(30)

    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                return

def draw_board(board, offset_x, title):
    label = FONT.render(f"{title}  Score: {board.score}", True, (255,255,255))
    screen.blit(label, (offset_x,20))
    for r in range(SIZE):
        for c in range(SIZE):
            v = board.grid[r][c]
            x = offset_x + c*(TILE+GAP)
            y = 60 + r*(TILE+GAP)
            pygame.draw.rect(screen, COLORS.get(v,(255,255,255)), (x,y,TILE,TILE), border_radius=8)
            if v:
                txt = FONT.render(str(v), True, (50,50,50))
                screen.blit(txt, txt.get_rect(center=(x+TILE//2,y+TILE//2)))

while True:
    screen.fill((40,40,40))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        if e.type == pygame.KEYDOWN:
            direction = None
            if e.key in (pygame.K_w, pygame.K_UP): direction = "up"
            elif e.key in (pygame.K_s, pygame.K_DOWN): direction = "down"
            elif e.key in (pygame.K_a, pygame.K_LEFT): direction = "left"
            elif e.key in (pygame.K_d, pygame.K_RIGHT): direction = "right"

            if direction:
                if human.move(direction):
                    human.add_random()
                    move = ai_move(ai)
                    if move:
                        ai.move(move)
                        ai.add_random()

    draw_board(human, 40, "YOU")
    draw_board(ai, W//2+20, "AI")
    pygame.display.update()

    result = check_game_over(human, ai)
    if result:
        end_screen(result)
        human = Board()
        ai = Board()
        continue

    clock.tick(30)
