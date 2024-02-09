import cv2 as cv
import numpy as np


def select_path(E):
    M = np.zeros(E.shape)
    M[0, :] = E[0, :]
    for i in range(1, M.shape[0]):
        for j in range(0, M.shape[1]):
            if j == 0:
                M[i, j] = E[i, j] + min(M[i - 1, j], M[i - 1, j + 1])
            elif j == E.shape[1] - 1:
                M[i, j] = E[i, j] + min(M[i - 1, j], M[i - 1, j - 1])
            else:
                M[i, j] = E[i, j] + min(M[i - 1, j - 1], M[i - 1, j], M[i - 1, j + 1])
    line = M.shape[0] - 1
    col = np.argmin(M[line, :])
    path = [0 for i in range(line + 1)]
    path[line] = (line, col)
    for line in range(M.shape[0] - 2, -1, -1):
        if col == 0:
            if M[line, 0] > M[line, 1]:
                new_col = 1
            else:
                new_col = 0
        elif col == E.shape[1] - 1:
            if M[line, col] > M[line, col - 1]:
                new_col = col - 1
            else:
                new_col = col
        else:
            neighbours = np.array([M[line, col - 1], M[line, col], M[line, col + 1]])
            new_col = col + np.argmin(neighbours) - 1
        path[line] = (line, new_col)
        col = new_col
    return path


def compute_energy(img):
    """
    Calculeaza energia la fiecare pixel pe baza gradientului
    :param img: imaginea initiala
    :return:E - energia
    """
    E = np.zeros((img.shape[0], img.shape[1]))
    # TODO: scrieti codul
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(img_gray, ddepth=cv.CV_16S, dx=1, dy=0, borderType=cv.BORDER_CONSTANT)
    grad_y = cv.Sobel(img_gray, ddepth=cv.CV_16S, dx=0, dy=1, borderType=cv.BORDER_CONSTANT)

    abs_x = np.abs(grad_x)
    abs_y = np.abs(grad_y)
    E = abs_x + abs_y

    return E


def show_path(img, path):
    new_image = img.copy()
    for row, col in path:
        new_image[row, col] = (0, 0, 255)

    E = compute_energy(img)
    new_image_E = img.copy()
    new_image_E[:, :, 0] = E.copy()
    new_image_E[:, :, 1] = E.copy()
    new_image_E[:, :, 2] = E.copy()

    for row, col in path:
        new_image_E[row, col] = (0, 0, 255)
    cv.imshow("path img", np.uint8(new_image))
    cv.imshow("path E", np.uint8(new_image_E))
    cv.waitKey(1000)


def delete_path(img, path):
    """
    Elimina drumul vertical din imagine
    :param img: imaginea initiala
    :path - drumul vertical
    return: updated_img - imaginea initiala din care s-a eliminat drumul vertical
    """
    updated_img = np.zeros((img.shape[0], img.shape[1] - 1, img.shape[2]), np.uint8)
    for i in range(img.shape[0]):
        col = path[i][1]
        updated_img[i, :col] = img[i, :col].copy()
        updated_img[i, col:] = img[i, col + 1 :].copy()
    return updated_img


def delete_object(image: np.ndarray, x0, y0, w, h, debug: bool):
    img = image.copy()
    if w < h:
        num_pixels = w
        for i in range(num_pixels):
            print("Eliminam drumul vertical numarul %i dintr-un total de %d." % (i + 1, num_pixels))
            E = compute_energy(img)
            E2 = np.zeros(E.shape)
            E2[y0 : y0 + h, x0 : x0 + w] = -100000
            E = E + E2
            w = w - 1
            path = select_path(E)
            if debug:
                show_path(img, path)
            img = delete_path(img, path)
    else:
        num_pixels = h
        img = np.rot90(img, k=3)
        for i in range(num_pixels):
            print("Eliminam drumul vertical numarul %i dintr-un total de %d." % (i + 1, num_pixels))
            E = compute_energy(img)
            E2 = np.zeros((E.shape[1], E.shape[0]))
            E2[y0 : y0 + h, x0 : x0 + w] = -100000
            E2 = np.rot90(E2, k=3)
            E = E + E2
            h = h - 1
            path = select_path(E)
            if debug:
                show_path(img, path)
            img = delete_path(img, path)
        img = np.rot90(img, k=1)
    cv.destroyAllWindows()
    return img


def remove_object(image: np.ndarray, x0: int, y0: int, w: int, h: int, debug: bool) -> np.ndarray:
    return delete_object(image, x0, y0, w, h, debug)
